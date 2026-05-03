#!/usr/bin/env python3
"""Convert a Medium account export into Hugo-flavored Markdown posts.

Usage:
    python scripts/convert_medium.py <medium-export-dir> <hugo-site-dir>

Reads <medium-export-dir>/posts/*.html (skipping drafts), writes:
  - <hugo-site-dir>/content/posts/<slug>.md
  - <hugo-site-dir>/static/images/<medium-id>/<image>  (downloaded from CDN)
"""

from __future__ import annotations

import argparse
import concurrent.futures
import os
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

HASH_RE = re.compile(r"-([0-9a-f]{8,16})$")
DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_")


@dataclass
class Stats:
    converted: int = 0
    skipped_draft: int = 0
    skipped_empty: int = 0
    images_ok: int = 0
    images_failed: int = 0


class HugoConverter(MarkdownConverter):
    """Markdownify subclass that emits clean output for Hugo/Goldmark."""

    def convert_figure(self, el, text, parent_tags):
        # A <figure> wrapping a single <img> just becomes the img markdown plus
        # an italic caption line (matching how Medium displays it).
        img = el.find("img")
        caption = el.find("figcaption")
        out = ""
        if img is not None:
            out = self.process_tag(img, parent_tags)
        if caption is not None:
            cap = caption.get_text(" ", strip=True)
            if cap:
                out = f"{out}\n*{cap}*"
        return f"\n\n{out}\n\n" if out else ""


_HEX_BLOB_RE = re.compile(r"^[0-9a-f]{20,}$")


def slugify(text: str) -> str:
    """Unicode-aware slug. Keeps CJK and other word chars; lower-cases ASCII."""
    text = unicodedata.normalize("NFKC", text).strip().lower()
    text = re.sub(r"\s+", "-", text)
    # Keep word chars (incl. unicode letters), hyphens; drop everything else.
    text = re.sub(r"[^\w-]", "", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def derive_slug(filename_stem: str, title: str, canonical_url: str, medium_id: str) -> str:
    """Pick the cleanest slug we can find."""
    title_has_cjk = any(ord(c) > 127 for c in title)

    # For non-ASCII titles, the canonical URL slug is URL-encoded UTF-8 bytes
    # converted to lowercase hex (eg `e5889de68ea2-line-message-api`), which is
    # ugly. Prefer the title itself in that case so the slug stays readable.
    if not title_has_cjk and canonical_url:
        path = urlparse(canonical_url).path.rstrip("/")
        last = path.rsplit("/", 1)[-1]
        if last.endswith(medium_id):
            last = last[: -len(medium_id)].rstrip("-")
        if last and last != medium_id and not _HEX_BLOB_RE.match(last):
            slug = slugify(last)
            if slug:
                return slug

    # Title-based slug (preserves CJK characters)
    slug = slugify(title)
    if slug:
        return slug

    # Filename stem with date + hash stripped
    stem = DATE_PREFIX_RE.sub("", filename_stem)
    stem = HASH_RE.sub("", stem)
    slug = slugify(stem)
    if slug:
        return slug

    return f"post-{medium_id}"


def safe_image_name(url: str) -> str:
    name = os.path.basename(urlparse(url).path) or "img"
    # Sanitize for filesystem (Medium ids contain '*')
    name = re.sub(r"[^\w.\-]", "_", name)
    return name or "img"


def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.0 Safari/605.1.15"
        ),
    })
    adapter = requests.adapters.HTTPAdapter(pool_connections=16, pool_maxsize=16, max_retries=2)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    return s


SESSION = make_session()


import time as _time
import threading as _threading

_DL_LOCK = _threading.Lock()
_LAST_DL = [0.0]
_DL_MIN_GAP = 0.15  # seconds between requests, host-wide


def _throttle() -> None:
    with _DL_LOCK:
        delta = _time.monotonic() - _LAST_DL[0]
        if delta < _DL_MIN_GAP:
            _time.sleep(_DL_MIN_GAP - delta)
        _LAST_DL[0] = _time.monotonic()


def download_image(url: str, dest: Path) -> tuple[bool, str]:
    global SESSION
    if dest.exists() and dest.stat().st_size > 0:
        return True, ""
    last_err = ""
    for attempt in range(4):
        _throttle()
        try:
            r = SESSION.get(url, timeout=30, stream=True)
            if r.status_code in (403, 429, 503):
                last_err = f"{r.status_code}"
                # Drop pooled connections — Medium's CDN sometimes wedges a
                # session into a 403 state once it hits a rate limit.
                SESSION.close()
                SESSION = make_session()
                _time.sleep(2.0 * (attempt + 1))
                continue
            r.raise_for_status()
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_suffix(dest.suffix + ".part")
            with open(tmp, "wb") as f:
                for chunk in r.iter_content(chunk_size=64 * 1024):
                    if chunk:
                        f.write(chunk)
            tmp.rename(dest)
            return True, ""
        except Exception as e:
            last_err = str(e)
            _time.sleep(2.0 * (attempt + 1))
    return False, last_err


def collect_image_jobs(body: BeautifulSoup, medium_id: str, images_root: Path) -> list[tuple[str, Path, "Tag"]]:
    jobs = []
    for img in body.find_all("img"):
        src = img.get("src")
        if not src or not src.startswith("http"):
            continue
        name = safe_image_name(src)
        dest = images_root / medium_id / name
        jobs.append((src, dest, img))
    return jobs


def transform_body(soup: BeautifulSoup, body, medium_id: str, images_root: Path, image_queue: list) -> None:
    """Mutate <body> tree in-place: rewrite img src to local path, simplify embeds.

    Image *downloads* are deferred — we just enqueue (url, dest) pairs. This lets
    us drive downloads serially after all conversions finish, which is the only
    reliable way past Medium CDN's per-IP rate limit.
    """
    jobs = collect_image_jobs(body, medium_id, images_root)
    for url, dest, img in jobs:
        img["src"] = f"/images/{medium_id}/{dest.name}"
        image_queue.append((url, dest))

    # 2) Mixtape embeds → simple link
    for div in body.select("div.graf--mixtapeEmbed"):
        a = div.find("a", href=True)
        if a is None:
            div.decompose()
            continue
        href = a["href"]
        title = ""
        strong = a.find("strong")
        if strong:
            title = strong.get_text(" ", strip=True)
        if not title:
            title = href
        new_p = soup.new_tag("p")
        link = soup.new_tag("a", href=href)
        link.string = title
        new_p.append(link)
        div.replace_with(new_p)

    # 3) Gist / iframe figures → link
    for fig in body.select("figure.graf--iframe"):
        script = fig.find("script", src=True)
        if script and "gist.github.com" in script["src"]:
            gist_url = script["src"]
            if gist_url.endswith(".js"):
                gist_url = gist_url[:-3]
            new_p = soup.new_tag("p")
            link = soup.new_tag("a", href=gist_url)
            link.string = "View gist"
            new_p.append(link)
            fig.replace_with(new_p)
        else:
            # Unknown iframe figure: just drop and log
            fig.decompose()


def toml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_frontmatter(*, title: str, date: str, subtitle: str, slug: str, canonical: str, medium_id: str) -> str:
    lines = ["+++"]
    lines.append(f'title = "{toml_escape(title)}"')
    lines.append(f'date = "{date}"')
    if subtitle:
        lines.append(f'description = "{toml_escape(subtitle)}"')
    lines.append(f'slug = "{slug}"')
    if canonical:
        lines.append(f'canonicalURL = "{canonical}"')
    lines.append(f'mediumID = "{medium_id}"')
    lines.append("+++\n\n")
    return "\n".join(lines)


def convert_file(path: Path, hugo_root: Path, stats: Stats, used_slugs: set[str], image_queue: list) -> None:
    name = path.name
    if name.startswith("draft_"):
        stats.skipped_draft += 1
        return

    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    title_el = soup.select_one("h1.p-name")
    title = title_el.get_text(" ", strip=True) if title_el else path.stem

    subtitle_el = soup.select_one('section[data-field="subtitle"]')
    subtitle = subtitle_el.get_text(" ", strip=True) if subtitle_el else ""

    time_el = soup.select_one("time.dt-published")
    date = time_el.get("datetime") if time_el else ""

    canonical_el = soup.select_one("a.p-canonical")
    canonical = canonical_el.get("href") if canonical_el else ""

    # Filename stem: drop .html
    stem = path.stem
    m = HASH_RE.search(stem)
    medium_id = m.group(1) if m else stem.rsplit("_", 1)[-1]

    body_el = soup.select_one('section[data-field="body"]')
    if body_el is None:
        stats.skipped_empty += 1
        print(f"  ! no body: {name}", file=sys.stderr)
        return

    images_root = hugo_root / "static" / "images"
    transform_body(soup, body_el, medium_id, images_root, image_queue)

    converter = HugoConverter(
        heading_style="ATX",
        bullets="-",
        code_language="",
        strip=["script", "style"],
    )
    body_html = body_el.decode_contents()
    md_body = converter.convert(body_html).strip()

    # Medium prepends a `<hr>` section divider and a duplicate `<h3>` title
    # before every body. Strip both so the post starts at the actual content.
    lines = md_body.splitlines()

    def _drop_leading_noise() -> None:
        while lines:
            stripped = lines[0].strip()
            if stripped == "" or stripped == "---" or stripped == "* * *":
                lines.pop(0)
            else:
                break

    _drop_leading_noise()

    def _norm(s: str) -> str:
        return re.sub(r"\s+", " ", s, flags=re.UNICODE).strip().lower()

    if lines and _norm(lines[0].lstrip("#")) == _norm(title):
        lines.pop(0)
        _drop_leading_noise()
    md_body = "\n".join(lines)

    # Pick a unique slug
    slug = derive_slug(stem, title, canonical, medium_id)
    base = slug
    counter = 2
    while slug in used_slugs:
        slug = f"{base}-{counter}"
        counter += 1
    used_slugs.add(slug)

    frontmatter = build_frontmatter(
        title=title,
        date=date,
        subtitle=subtitle,
        slug=slug,
        canonical=canonical,
        medium_id=medium_id,
    )

    out_path = hugo_root / "content" / "posts" / f"{slug}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter + md_body + "\n", encoding="utf-8")
    stats.converted += 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("export_dir", type=Path)
    parser.add_argument("hugo_root", type=Path)
    parser.add_argument("--limit", type=int, default=0, help="Convert only first N posts (debug)")
    args = parser.parse_args()

    posts_dir = args.export_dir / "posts"
    if not posts_dir.is_dir():
        print(f"posts dir not found: {posts_dir}", file=sys.stderr)
        return 2

    files = sorted(p for p in posts_dir.iterdir() if p.suffix == ".html")
    if args.limit:
        files = files[: args.limit]

    stats = Stats()
    used_slugs: set[str] = set()
    image_queue: list[tuple[str, Path]] = []
    for i, path in enumerate(files, 1):
        try:
            convert_file(path, args.hugo_root, stats, used_slugs, image_queue)
        except Exception as e:
            print(f"  ! failed {path.name}: {e}", file=sys.stderr)
        if i % 25 == 0:
            print(f"  …{i}/{len(files)} processed", file=sys.stderr)

    # Dedupe image queue by destination
    seen = set()
    unique_jobs = []
    for url, dest in image_queue:
        key = str(dest)
        if key in seen:
            continue
        seen.add(key)
        unique_jobs.append((url, dest))

    print(f"\nDownloading {len(unique_jobs)} unique images…", file=sys.stderr)
    failed_log = args.hugo_root / "scripts" / "failed_images.txt"
    failed_log.parent.mkdir(parents=True, exist_ok=True)
    with open(failed_log, "w") as flog:
        for j, (url, dest) in enumerate(unique_jobs, 1):
            ok, err = download_image(url, dest)
            if ok:
                stats.images_ok += 1
            else:
                stats.images_failed += 1
                flog.write(f"{url}\t{dest}\t{err}\n")
                print(f"  ! image failed: {url} ({err})", file=sys.stderr)
            if j % 50 == 0:
                print(
                    f"  …{j}/{len(unique_jobs)} images "
                    f"({stats.images_ok} ok, {stats.images_failed} failed)",
                    file=sys.stderr,
                )

    print(
        f"\nDone: {stats.converted} converted, {stats.skipped_draft} drafts skipped, "
        f"{stats.skipped_empty} empty skipped, {stats.images_ok} images downloaded, "
        f"{stats.images_failed} image failures"
    )
    if stats.images_failed:
        print(f"Failed image log: {failed_log}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

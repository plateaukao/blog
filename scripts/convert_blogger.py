#!/usr/bin/env python3
"""Convert a Blogger (Google Takeout) export into Hugo-flavored Markdown posts.

Usage:
    python scripts/convert_blogger.py <takeout-blogger-dir> <hugo-site-dir>

For each blog under <takeout-blogger-dir>/Blogs/*/feed.atom this reads every
LIVE POST entry (drafts, pages, comments and trashed posts are skipped) and
writes:
  - <hugo-site-dir>/content/posts/<slug>.md
  - <hugo-site-dir>/static/images/blogger/<post-id>/<image>  (downloaded)

Slugs are de-duplicated against each other *and* against the posts already in
content/posts, so an existing Medium-imported post is never overwritten — a
colliding Blogger post gets a "-2" suffix instead.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

ATOM = "http://www.w3.org/2005/Atom"
BLOGGER = "http://schemas.google.com/blogger/2018"
NS = {"a": ATOM, "b": BLOGGER}

HASH_RE = re.compile(r"-([0-9a-f]{8,16})$")


@dataclass
class Stats:
    converted: int = 0
    skipped_draft: int = 0
    skipped_nonpost: int = 0
    skipped_trashed: int = 0
    skipped_empty: int = 0
    images_ok: int = 0
    images_failed: int = 0
    blogs: list[str] = field(default_factory=list)


class HugoConverter(MarkdownConverter):
    """Markdownify subclass that emits clean output for Hugo/Goldmark."""

    def convert_figure(self, el, text, parent_tags):
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


def slugify(text: str) -> str:
    """Unicode-aware slug. Keeps CJK and other word chars; lower-cases ASCII."""
    text = unicodedata.normalize("NFKC", text).strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^\w-]", "", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def safe_image_name(url: str) -> str:
    name = os.path.basename(urlparse(url).path) or "img"
    name = re.sub(r"[^\w.\-]", "_", name)
    if "." not in name:
        name += ".jpg"
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
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=24, pool_maxsize=24, max_retries=2
    )
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    return s


SESSION = make_session()


def _flickr_live_fallback(url: str) -> str | None:
    """Old `farmN.static.flickr.com/...` URLs are flaky; the modern
    `live.staticflickr.com/...` host serves the same path. Return a rewritten
    URL to retry with, or None if not a flickr static URL."""
    p = urlparse(url)
    if re.match(r"farm\d+\.static\.?flickr\.com$", p.netloc) or p.netloc in (
        "static.flickr.com",
        "www.static.flickr.com",
    ):
        return f"https://live.staticflickr.com{p.path}"
    return None


def download_image(url: str, dest: Path) -> tuple[bool, str]:
    global SESSION
    if dest.exists() and dest.stat().st_size > 0:
        return True, ""
    candidates = [url]
    fb = _flickr_live_fallback(url)
    if fb:
        candidates.append(fb)
    last_err = ""
    for candidate in candidates:
        for attempt in range(3):
            try:
                r = SESSION.get(candidate, timeout=30, stream=True)
                if r.status_code in (403, 429, 503):
                    last_err = f"HTTP {r.status_code}"
                    SESSION.close()
                    SESSION = make_session()
                    continue
                r.raise_for_status()
                ctype = r.headers.get("Content-Type", "")
                if "text/html" in ctype:
                    last_err = f"not an image ({ctype})"
                    break
                dest.parent.mkdir(parents=True, exist_ok=True)
                tmp = dest.with_suffix(dest.suffix + ".part")
                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(chunk_size=64 * 1024):
                        if chunk:
                            f.write(chunk)
                if tmp.stat().st_size == 0:
                    tmp.unlink(missing_ok=True)
                    last_err = "empty body"
                    break
                tmp.rename(dest)
                return True, ""
            except Exception as e:  # noqa: BLE001
                last_err = str(e)
    return False, last_err


def toml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_frontmatter(
    *,
    title: str,
    date: str,
    description: str,
    slug: str,
    canonical: str,
    blogger_id: str,
    tags: list[str],
    cover: str | None,
) -> str:
    lines = ["+++"]
    lines.append(f'title = "{toml_escape(title)}"')
    lines.append(f'date = "{date}"')
    if description:
        lines.append(f'description = "{toml_escape(description)}"')
    lines.append(f'slug = "{slug}"')
    if canonical:
        lines.append(f'canonicalURL = "{canonical}"')
    lines.append(f'bloggerID = "{blogger_id}"')
    if tags:
        arr = ", ".join(f'"{toml_escape(t)}"' for t in tags)
        lines.append(f"tags = [{arr}]")
    if cover:
        lines.append("[cover]")
        lines.append(f'  image = "{cover}"')
    lines.append("+++\n\n")
    return "\n".join(lines)


def el_text(entry, path: str) -> str:
    el = entry.find(path, NS)
    return (el.text or "").strip() if el is not None else ""


def post_id_from_entry(entry) -> str:
    raw = el_text(entry, "a:id")
    m = re.search(r"post-(\d+)", raw)
    return m.group(1) if m else re.sub(r"\W+", "", raw)[-16:] or "unknown"


FIRST_IMG_MD = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def collect_blog_dirs(blogger_dir: Path) -> list[Path]:
    blogs_root = blogger_dir / "Blogs"
    return sorted(p for p in blogs_root.iterdir() if (p / "feed.atom").is_file())


def blog_subdomain(blog_dir: Path) -> str:
    settings = blog_dir / "settings.csv"
    if settings.is_file():
        with open(settings, newline="") as f:
            rows = list(csv.DictReader(f))
        if rows:
            return rows[0].get("blog_subdomain", "") or ""
    return ""


def convert_entry(
    entry,
    *,
    subdomain: str,
    hugo_root: Path,
    stats: Stats,
    used_slugs: set[str],
    image_queue: list,
) -> None:
    etype = el_text(entry, "b:type")
    if etype != "POST":
        stats.skipped_nonpost += 1
        return
    status = el_text(entry, "b:status")
    if status != "LIVE":
        stats.skipped_draft += 1
        return
    trashed_el = entry.find("b:trashed", NS)
    if trashed_el is not None and (trashed_el.text or "").strip():
        stats.skipped_trashed += 1
        return

    blogger_id = post_id_from_entry(entry)
    title = el_text(entry, "a:title") or f"untitled-{blogger_id}"
    date = el_text(entry, "a:published")
    description = el_text(entry, "b:metaDescription")
    filename = el_text(entry, "b:filename")
    canonical = (
        f"https://{subdomain}.blogspot.com{filename}"
        if subdomain and filename
        else ""
    )
    tags = [
        c.get("term", "").strip()
        for c in entry.findall("a:category", NS)
        if c.get("term", "").strip()
    ]

    content_el = entry.find("a:content", NS)
    html = content_el.text if content_el is not None and content_el.text else ""
    if not html.strip():
        stats.skipped_empty += 1
        return

    soup = BeautifulSoup(html, "html.parser")
    images_root = hugo_root / "static" / "images" / "blogger"

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src or not src.startswith("http"):
            continue
        name = safe_image_name(src)
        dest = images_root / blogger_id / name
        img["src"] = f"/images/blogger/{blogger_id}/{name}"
        image_queue.append((src, dest))

    # YouTube / generic iframes → plain link (markdownify would drop them).
    for ifr in soup.find_all("iframe"):
        src = ifr.get("src", "")
        if not src:
            ifr.decompose()
            continue
        p = soup.new_tag("p")
        a = soup.new_tag("a", href=src)
        a.string = "View video" if "youtube" in src or "youtu.be" in src else src
        p.append(a)
        ifr.replace_with(p)

    converter = HugoConverter(
        heading_style="ATX",
        bullets="-",
        code_language="",
        strip=["script", "style"],
    )
    md_body = converter.convert(str(soup)).strip()
    md_body = re.sub(r"\n{3,}", "\n\n", md_body)

    # Drop a leading duplicate of the title if the body opens with it.
    lines = md_body.splitlines()

    def _norm(s: str) -> str:
        return re.sub(r"\s+", " ", s, flags=re.UNICODE).strip().lower()

    while lines and lines[0].strip() in ("", "---", "* * *"):
        lines.pop(0)
    if lines and _norm(lines[0].lstrip("#")) == _norm(title):
        lines.pop(0)
        while lines and lines[0].strip() in ("", "---", "* * *"):
            lines.pop(0)
    md_body = "\n".join(lines)

    cover_m = FIRST_IMG_MD.search(md_body)
    cover = cover_m.group(1) if cover_m else None

    base = slugify(title) or (
        slugify(Path(filename).stem) if filename else ""
    ) or f"post-{blogger_id}"
    slug = base
    counter = 2
    while slug in used_slugs:
        slug = f"{base}-{counter}"
        counter += 1
    used_slugs.add(slug)

    frontmatter = build_frontmatter(
        title=title,
        date=date,
        description=description,
        slug=slug,
        canonical=canonical,
        blogger_id=blogger_id,
        tags=tags,
        cover=cover,
    )
    out_path = hugo_root / "content" / "posts" / f"{slug}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter + md_body + "\n", encoding="utf-8")
    stats.converted += 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("blogger_dir", type=Path)
    parser.add_argument("hugo_root", type=Path)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument(
        "--skip-images", action="store_true", help="convert posts only"
    )
    args = parser.parse_args()

    posts_dir = args.hugo_root / "content" / "posts"
    # Seed used slugs with existing posts so we never clobber them.
    used_slugs: set[str] = set()
    for p in posts_dir.glob("*.md"):
        used_slugs.add(p.stem)
        txt = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r'^slug = "([^"]+)"', txt, re.M)
        if m:
            used_slugs.add(m.group(1))
    print(f"Seeded {len(used_slugs)} existing slug(s)", file=sys.stderr)

    stats = Stats()
    image_queue: list[tuple[str, Path]] = []

    blog_dirs = collect_blog_dirs(args.blogger_dir)
    for blog_dir in blog_dirs:
        subdomain = blog_subdomain(blog_dir)
        stats.blogs.append(f"{blog_dir.name} ({subdomain or 'no-subdomain'})")
        root = ET.parse(blog_dir / "feed.atom").getroot()
        entries = root.findall("a:entry", NS)
        if args.limit:
            entries = entries[: args.limit]
        for i, entry in enumerate(entries, 1):
            try:
                convert_entry(
                    entry,
                    subdomain=subdomain,
                    hugo_root=args.hugo_root,
                    stats=stats,
                    used_slugs=used_slugs,
                    image_queue=image_queue,
                )
            except Exception as e:  # noqa: BLE001
                print(f"  ! failed entry: {e}", file=sys.stderr)
            if i % 200 == 0:
                print(
                    f"  …{blog_dir.name}: {i}/{len(entries)}", file=sys.stderr
                )

    # Dedupe image jobs by destination.
    seen: set[str] = set()
    jobs: list[tuple[str, Path]] = []
    for url, dest in image_queue:
        key = str(dest)
        if key in seen:
            continue
        seen.add(key)
        jobs.append((url, dest))

    if not args.skip_images:
        print(f"\nDownloading {len(jobs)} unique images…", file=sys.stderr)
        failed_log = args.hugo_root / "scripts" / "failed_blogger_images.txt"
        done = 0
        with open(failed_log, "w") as flog, concurrent.futures.ThreadPoolExecutor(
            max_workers=12
        ) as ex:
            fut = {ex.submit(download_image, u, d): (u, d) for u, d in jobs}
            for f in concurrent.futures.as_completed(fut):
                u, d = fut[f]
                ok, err = f.result()
                if ok:
                    stats.images_ok += 1
                else:
                    stats.images_failed += 1
                    flog.write(f"{u}\t{d}\t{err}\n")
                done += 1
                if done % 100 == 0:
                    print(
                        f"  …{done}/{len(jobs)} images "
                        f"({stats.images_ok} ok, {stats.images_failed} failed)",
                        file=sys.stderr,
                    )

    print(
        "\nDone.\n"
        f"  Blogs:            {', '.join(stats.blogs)}\n"
        f"  Converted:        {stats.converted}\n"
        f"  Skipped draft:    {stats.skipped_draft}\n"
        f"  Skipped non-post: {stats.skipped_nonpost}\n"
        f"  Skipped trashed:  {stats.skipped_trashed}\n"
        f"  Skipped empty:    {stats.skipped_empty}\n"
        f"  Images OK:        {stats.images_ok}\n"
        f"  Images failed:    {stats.images_failed}"
    )
    if stats.images_failed:
        print(
            "  Failed images logged to scripts/failed_blogger_images.txt",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

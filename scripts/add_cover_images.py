#!/usr/bin/env python3
"""Populate `[cover] image = ...` in each post's TOML front matter,
using the first inline ![](path) image found in the body.

Idempotent: skips posts that already have a cover image set.
"""
from __future__ import annotations
import re
from pathlib import Path

POSTS = Path(__file__).resolve().parent.parent / "content" / "posts"
FM_DELIM = "+++"
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def split_frontmatter(text: str) -> tuple[str, str, str] | None:
    """Return (fm_inner, closing_and_after, full_match_offset_unused).

    fm_inner: everything between the opening +++ and the closing +++,
              not including either delimiter.
    rest:     the closing +++ delimiter and everything after.
    """
    if not text.startswith(FM_DELIM + "\n"):
        return None
    inner_start = len(FM_DELIM) + 1  # past "+++\n"
    close_idx = text.find(f"\n{FM_DELIM}\n", inner_start)
    if close_idx == -1:
        return None
    fm_inner = text[inner_start:close_idx + 1]  # include trailing newline
    rest = text[close_idx + 1:]  # starts with "+++\n"
    return fm_inner, rest, ""


def already_has_cover(fm_inner: str) -> bool:
    return "[cover]" in fm_inner


def first_image(body: str) -> str | None:
    m = IMG_RE.search(body)
    return m.group(1) if m else None


def main() -> None:
    updated = 0
    skipped_existing = 0
    skipped_no_image = 0
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        parts = split_frontmatter(text)
        if not parts:
            continue
        fm_inner, rest, _ = parts
        if already_has_cover(fm_inner):
            skipped_existing += 1
            continue
        body = rest[len(FM_DELIM) + 1:]  # past closing "+++\n"
        img = first_image(body)
        if not img:
            skipped_no_image += 1
            continue
        cover_block = f'[cover]\n  image = "{img}"\n'
        new_text = (
            FM_DELIM + "\n" + fm_inner + cover_block + rest
        )
        path.write_text(new_text, encoding="utf-8")
        updated += 1

    print(f"Updated:           {updated}")
    print(f"Skipped (had cover): {skipped_existing}")
    print(f"Skipped (no image):  {skipped_no_image}")


if __name__ == "__main__":
    main()

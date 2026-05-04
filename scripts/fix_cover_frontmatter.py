#!/usr/bin/env python3
"""Repair posts where add_cover_images.py produced a duplicate closing
+++ before the [cover] block.

Bad shape:

    +++
    ... fm fields ...
    +++
    [cover]
      image = "..."
    +++

Target shape:

    +++
    ... fm fields ...
    [cover]
      image = "..."
    +++
"""
from __future__ import annotations
from pathlib import Path

POSTS = Path(__file__).resolve().parent.parent / "content" / "posts"
BAD = "+++\n[cover]\n"
GOOD = "[cover]\n"


def main() -> None:
    fixed = 0
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if BAD not in text:
            continue
        # only replace the first occurrence (the one inside front matter)
        new_text = text.replace(BAD, GOOD, 1)
        path.write_text(new_text, encoding="utf-8")
        fixed += 1
    print(f"Fixed: {fixed}")


if __name__ == "__main__":
    main()

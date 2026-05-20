---
name: post-add
description: Publish a local (Obsidian-style) Markdown file as a new post in this Hugo/PaperMod blog — converts front matter and image embeds, copies and optimizes images, builds, then commits and pushes to origin/main (no ADR). Trigger when the user runs /post-add with a path to a local .md file (optionally with tag names) and wants it added to the blog.
metadata:
  author: Daniel Kao
  keywords:
  - hugo
  - blog post
  - obsidian
  - publish
---

# post-add

Turn a local Markdown file (typically an Obsidian note) into a published post
in this Hugo + PaperMod blog, then commit and push.

## Arguments

`/post-add <path-to-.md-file> [tag ...]`

- **Path** may contain spaces — always quote it. Example:
  `/post-add "/Users/maoyuankao/My Documents/blogs/knowledge/Foo.md" 電子書閱讀器`
- **Tags** (optional) are everything after the path. If the user gave tags in
  prose instead ("add the 電子書閱讀器 tag"), use those. If no tag is given,
  ask the user for one before committing.

## Workflow (do these in order)

- [ ] **1. Read the source file.** `cat` the given `.md`. Note its directory
  (`SRCDIR`) — Obsidian attachments usually live there.

- [ ] **2. Derive metadata.**
  - **title**: the source's first H1 if present, else the file's base name
    (without `.md`), spaces preserved.
  - **date**: `date -u +"%Y-%m-%dT%H:%M:%S.000Z"` (current UTC).
  - **slug**: title → lowercase ASCII letters/digits, spaces → `-`, drop dots
    and other punctuation, **keep CJK characters as-is**. Match the repo's
    existing style (e.g. `在-macos-上跑-llamacpp-server-並使用-mixtral-8x7b-llm-model`).
  - **description**: a concise 1–2 sentence summary in the post's own
    language.
  - **tags**: from the arguments. **Before using a tag, check it against
    existing tags** so you reuse the exact existing spelling/casing instead of
    creating a near-duplicate:
    `grep -rh 'tags = ' content/posts --include='*.md' | grep -i '<tag>'`

- [ ] **3. Collect & optimize images.** For every Obsidian embed `![[NAME]]`
  in the body (in order):
  - Find `NAME` in `SRCDIR` first, then search recursively upward from there
    (the Obsidian vault) if missing. If an image can't be found, stop and tell
    the user.
  - Copy into `static/images/<slug>/`.
  - **Rename** any file whose name has spaces or non-URL-safe characters to a
    short descriptive kebab-case name (infer meaning from surrounding text).
  - **Optimize with `sips`** (no ImageMagick on this machine):
    - If width > 1400: `sips --resampleWidth 1400 ...`
    - Convert oversized PNG screenshots to JPEG:
      `sips --resampleWidth 1400 -s format jpeg -s formatOptions 85 in.png --out out.jpg` then `rm in.png`
    - Re-compress large JPEGs the same way. Aim for ~150–350 KB each, in line
      with the blog's other images.

- [ ] **4. Write the post** to `content/posts/<slug>.md` with **TOML `+++`**
  front matter in this exact field order (this is an original post — do **not**
  add `canonicalURL`/`bloggerID`/`mediumID`):
  ```
  +++
  title = "<title>"
  date = "<utc-timestamp>"
  description = "<summary>"
  slug = "<slug>"
  tags = ["<tag>", ...]
  [cover]
    image = "/images/<slug>/<first-image-filename>"
  +++
  ```
  Then the body: copy the source text **verbatim**, only rewriting each
  `![[NAME]]` → `![](/images/<slug>/<final-filename>)`. Leave plain-text URLs
  and all other content untouched. `[cover].image` must be the **first** inline
  image (drives the listing thumbnail and the og:image / Twitter card).

  **Paragraph spacing.** Obsidian renders a single line break between two text
  lines as a paragraph break, but Hugo's Goldmark joins them into one paragraph.
  So when consecutive non-empty text lines in the source are clearly distinct
  paragraphs (different sentences, different topics), insert a blank line
  between them. Also leave blank lines around fenced code blocks, image lines,
  and headings. Don't touch line wrapping inside what is genuinely one
  paragraph.

- [ ] **5. Build & verify.** `HUGO_ENV=production hugo --quiet --environment production`,
  then on `public/posts/<slug>/index.html` confirm:
  - the page built;
  - `og:image` and every inline `src` use the full `https://…/blog/images/…`
    path (the project overrides in `layouts/_partials/templates/` handle this);
  - the post appears on `public/index.html` and on
    `public/tags/<tag>/index.html`.
  Fix anything that fails before continuing.

- [ ] **6. Commit & push.** Stage only the new post and its image dir:
  ```
  git add "content/posts/<slug>.md" static/images/<slug>/
  ```
  Commit on `main` (this repo's established workflow — commit directly to
  `main`, do not branch) with message:
  ```
  Add post: <title>

  <one short line on the post and its tag(s)>

  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
  ```
  Then `git push origin main`.

- [ ] **7. NO ADR.** Skip the global post-commit ADR rule — this repo is
  exempt (see the blog's auto-memory). Do not create anything under `~/src/ADR/`.

## Notes

- All paths are relative to the blog repo root `/Users/maoyuankao/src/blog`.
- Don't stage unrelated working-tree changes — add only the post and its images.
- Report a short summary: slug, tag(s) used, image count/sizes, commit hash.

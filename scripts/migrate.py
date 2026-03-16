#!/usr/bin/env python3
"""Migrate Jekyll posts to Astro AstroPaper format."""

import os
import re
import sys
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "_posts"
OUTPUT_DIR = Path(__file__).parent.parent / "src" / "data" / "blog"

REMOVE_KEYS = {"layout", "comments", "typora-root-url", "use_math", "categories"}


def parse_frontmatter(content: str):
    """Parse YAML frontmatter and return (frontmatter_dict_raw, body)."""
    content = content.lstrip("\n\r\ufeff")  # handle BOM and leading newlines
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 4:].lstrip("\n")
    return fm_text, body


def parse_yaml_simple(fm_text: str) -> dict:
    """Very simple YAML parser for flat + list values."""
    result = {}
    lines = fm_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.startswith("#"):
            i += 1
            continue
        m = re.match(r'^(\w[\w-]*)\s*:\s*(.*)', line.rstrip())
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            # Inline list: tags: [a, b]
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1]
                items = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
                result[key] = items
            else:
                result[key] = val.strip("'\"")
        i += 1
    return result


def extract_description(body: str) -> str:
    """Extract first meaningful paragraph as description."""
    lines = body.split("\n")
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("---") or line.startswith("```"):
            continue
        if line.startswith("###") or line.startswith("##") or line.startswith("#"):
            continue
        # Skip summary headers like "### Summary"
        if re.match(r'^#+\s', line):
            continue
        # Remove markdown formatting for description
        desc = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        desc = re.sub(r'\*(.+?)\*', r'\1', desc)
        desc = re.sub(r'`(.+?)`', r'\1', desc)
        desc = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', desc)
        desc = desc.strip()
        if len(desc) > 20:
            return desc[:200]
    return ""


def migrate_post(src: Path, dst_dir: Path):
    content = src.read_text(encoding="utf-8")
    fm_text, body = parse_frontmatter(content)
    if isinstance(fm_text, dict):
        print(f"  [WARN] No frontmatter: {src.name}")
        fm = {}
    else:
        fm = parse_yaml_simple(fm_text)

    # Extract date from filename: YYYY-MM-DD-slug.md
    m = re.match(r'^(\d{4}-\d{2}-\d{2})-(.+)\.md$', src.name)
    if m:
        date_str = m.group(1)
        slug = m.group(2)
    else:
        date_str = "2020-01-01"
        slug = src.stem

    # Build new frontmatter
    new_fm = {}

    # title
    title = fm.get("title", slug).strip('"\'')
    new_fm["title"] = title

    # description (subtitle → description, fallback to body extract)
    description = fm.get("subtitle", "").strip('"\'')
    if not description:
        description = extract_description(body)
    new_fm["description"] = description

    # author
    author = fm.get("author", "Pebpung").strip('"\'')
    new_fm["author"] = author

    # pubDatetime
    new_fm["pubDatetime"] = f"{date_str}T09:00:00"

    # tags: merge tags + categories
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    categories = fm.get("categories", "")
    if categories and isinstance(categories, str):
        for cat in [c.strip() for c in categories.split(",")]:
            if cat and cat not in tags:
                tags.append(cat)
    if not tags:
        tags = ["others"]
    new_fm["tags"] = tags

    # draft: default false
    # new_fm["draft"] = False  # omit — defaults fine

    # Build output YAML manually (keep it simple)
    lines = ["---"]
    lines.append(f"title: {quote_yaml(title)}")
    lines.append(f"description: {quote_yaml(description)}")
    lines.append(f"author: {quote_yaml(author)}")
    lines.append(f"pubDatetime: {new_fm['pubDatetime']}")
    tag_list = ", ".join(new_fm["tags"])
    lines.append(f"tags: [{tag_list}]")
    lines.append("---")

    new_content = "\n".join(lines) + "\n\n" + body

    dst = dst_dir / src.name
    dst.write_text(new_content, encoding="utf-8")
    print(f"  ✓ {src.name}")


def quote_yaml(s: str) -> str:
    """Quote a string for YAML if it contains special chars."""
    if any(c in s for c in [':', '#', '[', ']', '{', '}', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]):
        # Use double quotes, escape internal double quotes
        s_escaped = s.replace('"', '\\"')
        return f'"{s_escaped}"'
    return s


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    posts = sorted(POSTS_DIR.glob("*.md"))
    print(f"Migrating {len(posts)} posts...")
    for post in posts:
        migrate_post(post, OUTPUT_DIR)
    print(f"\nDone! {len(posts)} posts written to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

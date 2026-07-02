#!/usr/bin/env python3
"""Keep only _TOPICS folder entries in the book sidebar."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
BOOK_OUTPUT_DIR = BOOK_DIR / "_book"
SIDEBAR_PAGES_JSON = BOOK_DIR / "generated" / "sidebar-pages.json"
TOC_PATTERN = re.compile(
    r'(<ul class="book-toc list-unstyled">)(.*?)(</ul>)',
    re.DOTALL,
)
LI_PATTERN = re.compile(r"<li\b.*?</li>", re.DOTALL)
HREF_PATTERN = re.compile(r'href="([^"]+)"')


def filter_toc(html: str, allowed: set[str]) -> str:
    match = TOC_PATTERN.search(html)
    if not match:
        return html

    prefix, toc_body, suffix = match.groups()
    kept_items: list[str] = []

    for item in LI_PATTERN.findall(toc_body):
        href_match = HREF_PATTERN.search(item)
        if not href_match:
            continue
        href = href_match.group(1)
        if href in allowed:
            kept_items.append(item)

    filtered = prefix + "".join(kept_items) + suffix
    return html[: match.start()] + filtered + html[match.end() :]


def main() -> None:
    if not SIDEBAR_PAGES_JSON.is_file():
        raise RuntimeError(f"Missing sidebar manifest: {SIDEBAR_PAGES_JSON}")

    allowed = set(json.loads(SIDEBAR_PAGES_JSON.read_text(encoding="utf-8")))
    html_files = sorted(BOOK_OUTPUT_DIR.glob("*.html"))

    if not html_files:
        raise RuntimeError(f"No HTML files found in {BOOK_OUTPUT_DIR}")

    for path in html_files:
        if path.name == "404.html":
            continue
        html = path.read_text(encoding="utf-8")
        updated = filter_toc(html, allowed)
        if updated != html:
            path.write_text(updated, encoding="utf-8")

    print(f"Filtered sidebar in {len(html_files) - 1} pages.")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

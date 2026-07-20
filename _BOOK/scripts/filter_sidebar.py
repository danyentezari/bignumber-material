#!/usr/bin/env python3
"""Rebuild the book sidebar with topic folders and nested subtopics."""

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
LINK_PATTERN = re.compile(
    r'<a class="([^"]*)" href="([^"]+)"><span class="header-section-number">(\d+)</span>\s*(.*?)</a>',
    re.DOTALL,
)


def normalize_title(title: str) -> str:
    normalized = re.sub(r"\s+", " ", title.strip())
    for apostrophe in ("\u0027", "\u2019", "\u2018", "`"):
        normalized = normalized.replace(apostrophe, "'")
    return normalized.lower()


def parse_toc_links(toc_body: str) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    by_href: dict[str, dict[str, str]] = {}
    by_title: dict[str, dict[str, str]] = {}

    for match in LINK_PATTERN.finditer(toc_body):
        active_class, href, section_number, title = match.groups()
        normalized_title = normalize_title(title)
        item = {
            "href": href,
            "section_number": section_number,
            "title": re.sub(r"\s+", " ", title.strip()),
        }
        by_href[href] = item
        by_title[normalized_title] = item

    return by_href, by_title


def lookup_entry(
    entry: dict[str, object],
    by_href: dict[str, dict[str, str]],
    by_title: dict[str, dict[str, str]],
) -> dict[str, str] | None:
    href = entry.get("href")
    if isinstance(href, str) and href in by_href:
        return by_href[href]

    title = entry.get("title")
    if isinstance(title, str):
        return by_title.get(normalize_title(title))

    return None


def render_link(item: dict[str, str], current_href: str, label: str | None = None) -> str:
    active_class = "active" if item["href"] == current_href else ""
    text = label if label else item["title"]
    return (
        f'<a class="{active_class}" href="{item["href"]}">'
        f'<span class="header-section-number">{item["section_number"]}</span> '
        f"{text}</a>"
    )


def render_parent_link(
    item: dict[str, str],
    current_href: str,
    child_items: list[dict[str, str]],
    label: str | None = None,
) -> str:
    classes: list[str] = []
    if item["href"] == current_href:
        classes.append("active")
    elif any(child["href"] == current_href for child in child_items):
        classes.append("active-parent")
    active_class = " ".join(classes)
    class_attr = f' class="{active_class}"' if active_class else ' class=""'
    text = label if label else item["title"]
    return (
        f"<a{class_attr} href=\"{item['href']}\">"
        f'<span class="header-section-number">{item["section_number"]}</span> '
        f"{text}</a>"
    )


def build_sidebar_toc(
    sidebar: list[dict[str, object]],
    by_href: dict[str, dict[str, str]],
    by_title: dict[str, dict[str, str]],
    current_href: str,
) -> str:
    """Render root-level topics only; subtopics appear on main topic pages."""
    lines = ['<ul class="book-toc list-unstyled">']

    for entry in sidebar:
        main_item = lookup_entry(entry, by_href, by_title)
        if not main_item:
            continue

        children = entry.get("children", [])
        child_items: list[dict[str, str]] = []
        if isinstance(children, list):
            for child in children:
                if not isinstance(child, dict):
                    continue
                child_item = lookup_entry(child, by_href, by_title)
                if child_item:
                    child_items.append(child_item)

        label = entry.get("label")
        label_text = label if isinstance(label, str) else None

        lines.append('<li class="book-toc-topic book-toc-topic--leaf">')
        lines.append('<div class="book-toc-topic-header">')
        lines.append(
            '<span class="book-toc-toggle book-toc-toggle--placeholder" '
            'aria-hidden="true"></span>'
        )
        if child_items:
            lines.append(
                render_parent_link(main_item, current_href, child_items, label_text)
            )
        else:
            lines.append(render_link(main_item, current_href, label_text))
        lines.append("</div>")
        lines.append("</li>")

    lines.append("</ul>")
    return "\n".join(lines)


def current_page_href(html: str, toc_body: str) -> str | None:
    for match in LINK_PATTERN.finditer(toc_body):
        active_class, href, _, _ = match.groups()
        if "active" in active_class.split():
            return href

    title_match = re.search(r"<title>(\d+)\s+(.*?)\s+\|", html)
    if not title_match:
        return None

    page_title = title_match.group(2).strip()
    _, by_title = parse_toc_links(toc_body)
    item = by_title.get(normalize_title(page_title))
    return item["href"] if item else None


BREADCRUMB_SCRIPT_RE = re.compile(
    r'<script type="application/json" id="page-breadcrumbs">.*?</script>\n?',
    re.DOTALL,
)


def build_parent_map(
    sidebar: list[dict[str, object]],
    by_href: dict[str, dict[str, str]],
    by_title: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    parent_of: dict[str, dict[str, str]] = {}
    for entry in sidebar:
        main_item = lookup_entry(entry, by_href, by_title)
        if not main_item:
            continue
        children = entry.get("children", [])
        if not isinstance(children, list):
            continue
        for child in children:
            if not isinstance(child, dict):
                continue
            child_item = lookup_entry(child, by_href, by_title)
            if child_item:
                parent_of[child_item["href"]] = main_item
    return parent_of


def breadcrumb_trail(
    current_href: str,
    current_title: str,
    parent_of: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    """Breadcrumb trail including the current page as the final crumb."""
    if current_href == "index.html":
        return [{"title": "Home", "href": "index.html", "current": True}]

    trail: list[dict[str, object]] = [
        {"title": "Home", "href": "index.html", "current": False}
    ]
    parent = parent_of.get(current_href)
    if parent and parent["href"] != current_href:
        trail.append(
            {"title": parent["title"], "href": parent["href"], "current": False}
        )
    trail.append({"title": current_title, "href": current_href, "current": True})
    return trail


def inject_breadcrumb_data(html: str, trail: list[dict[str, object]]) -> str:
    payload = json.dumps(trail, ensure_ascii=True)
    script = (
        f'<script type="application/json" id="page-breadcrumbs">{payload}</script>\n'
    )
    html = BREADCRUMB_SCRIPT_RE.sub("", html)
    if "</head>" in html:
        return html.replace("</head>", script + "</head>", 1)
    return script + html


def rebuild_toc(html: str, sidebar: list[dict[str, object]]) -> str:
    match = TOC_PATTERN.search(html)
    if not match:
        return html

    prefix, toc_body, suffix = match.groups()
    by_href, by_title = parse_toc_links(toc_body)
    current_href = current_page_href(html, toc_body)
    if not current_href:
        return html

    rebuilt = build_sidebar_toc(sidebar, by_href, by_title, current_href)
    html = html[: match.start()] + rebuilt + html[match.end() :]

    parent_of = build_parent_map(sidebar, by_href, by_title)
    current_item = by_href.get(current_href)
    current_title = current_item["title"] if current_item else current_href
    trail = breadcrumb_trail(current_href, current_title, parent_of)
    return inject_breadcrumb_data(html, trail)


def load_sidebar_manifest() -> list[dict[str, object]]:
    raw = json.loads(SIDEBAR_PAGES_JSON.read_text(encoding="utf-8"))
    if isinstance(raw, list) and raw and all(isinstance(item, str) for item in raw):
        return [{"title": "", "href": href, "children": []} for href in raw]
    if not isinstance(raw, list):
        raise RuntimeError(f"Invalid sidebar manifest format: {SIDEBAR_PAGES_JSON}")
    return raw


def main() -> None:
    if not SIDEBAR_PAGES_JSON.is_file():
        raise RuntimeError(f"Missing sidebar manifest: {SIDEBAR_PAGES_JSON}")

    sidebar = load_sidebar_manifest()
    html_files = sorted(BOOK_OUTPUT_DIR.glob("*.html"))

    if not html_files:
        raise RuntimeError(f"No HTML files found in {BOOK_OUTPUT_DIR}")

    for path in html_files:
        if path.name == "404.html":
            continue
        html = path.read_text(encoding="utf-8")
        updated = rebuild_toc(html, sidebar)
        if updated != html:
            path.write_text(updated, encoding="utf-8")

    print(f"Rebuilt sidebar in {len(html_files) - 1} pages.")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

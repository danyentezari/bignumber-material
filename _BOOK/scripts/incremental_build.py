#!/usr/bin/env python3
"""
Incremental book rebuild for content edits.

Usage:
  python3 scripts/incremental_build.py --seed-cache
  python3 scripts/incremental_build.py --changed path1 [path2 ...]

Content-only topic edits: generate_topics → pandoc inplace splice →
sidebar/assets → Site Index + search refresh.

Structural changes (new/deleted pages, H1 renames, sidebar/chrome/scripts,
or any listed chapter missing HTML): fall back to ./build.sh.
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BOOK_DIR.parent
TOPICS_DIR = REPO_ROOT / "_TOPICS"
GENERATED_DIR = BOOK_DIR / "generated"
BOOK_OUT = BOOK_DIR / "_book"
BOOKDOWN_YML = BOOK_DIR / "_bookdown.yml"
TITLE_CACHE = GENERATED_DIR / ".watch-titles.json"
SEARCH_JSON = BOOK_OUT / "search.json"

STRUCTURAL_NAMES = frozenset(
    {
        "sidebar.txt",
        "index.Rmd",
        "head.html",
        "after_body.html",
        "style.css",
        "_output.yml",
        "published.txt",
        "pre-render.R",
        "post-render.R",
        "build.sh",
    }
)
STRUCTURAL_SCRIPT_PREFIXES = (
    "generate_topics.py",
    "filter_sidebar.py",
    "verify_book_coverage.py",
    "copy_topic_assets.py",
    "incremental_build.py",
)

TITLE_RE = re.compile(
    r"<title>(\d+)\s+(.*?)\s+\|\s*[^<]*</title>",
    re.IGNORECASE | re.DOTALL,
)
SECTION_RE = re.compile(
    r'<div\s+id="([^"]+)"\s+class="section\s+level(\d+)"[^>]*>',
    re.IGNORECASE,
)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def extract_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return path.stem.replace("-", " ")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem.replace("-", " ")


def slugify_text(text: str) -> str:
    """Match generate_topics / bookdown ASCII-safe chapter filenames."""
    normalized = unicodedata.normalize("NFKD", text)
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    normalized = (
        normalized.lower()
        .replace("'", "")
        .replace("\u2018", "")
        .replace("\u2019", "")
    )
    normalized = re.sub(r"[(),]", "", normalized)
    return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")


def normalize_title_key(text: str) -> str:
    return slugify_text(text)


def is_safe_md(path: Path) -> bool:
    return path.suffix.lower() == ".md" and re.fullmatch(
        r"[A-Za-z0-9._-]+\.md", path.name
    )


def list_topic_markdown() -> dict[str, str]:
    """Map repo-relative posix path -> H1 title for every topic .md."""
    titles: dict[str, str] = {}
    if not TOPICS_DIR.is_dir():
        return titles
    for folder in TOPICS_DIR.iterdir():
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if path.is_file() and is_safe_md(path):
                rel = path.relative_to(REPO_ROOT).as_posix()
                titles[rel] = extract_title(path)
    return titles


def load_title_cache() -> dict[str, str]:
    if not TITLE_CACHE.is_file():
        return {}
    try:
        data = json.loads(TITLE_CACHE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {str(k): str(v) for k, v in data.items()}


def save_title_cache(titles: dict[str, str]) -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    TITLE_CACHE.write_text(
        json.dumps(titles, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def resolve_changed(path_str: str) -> Path | None:
    path = Path(path_str)
    if not path.is_absolute():
        # Watcher may emit paths relative to _BOOK or absolute.
        candidates = [path, BOOK_DIR / path, REPO_ROOT / path]
        for candidate in candidates:
            try:
                resolved = candidate.resolve()
            except OSError:
                continue
            if resolved.exists() or candidate.as_posix().endswith(".md"):
                path = resolved
                break
        else:
            path = path.resolve() if path.exists() else (BOOK_DIR / path_str).resolve()
    else:
        path = path.resolve()
    return path


def is_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def classify_change(
    path: Path,
    cached_titles: dict[str, str],
    current_titles: dict[str, str],
) -> str:
    """Return 'structural', 'content', or 'ignore'."""
    name = path.name

    # Ignore outputs and junk.
    if is_under(path, BOOK_OUT) or is_under(path, GENERATED_DIR):
        return "ignore"
    if name in {".DS_Store", ".watch-titles.json"} or name.endswith("~"):
        return "ignore"
    if name.startswith(".") and path.suffix not in {".Rmd", ".R", ".yml", ".yaml"}:
        return "ignore"

    if name in STRUCTURAL_NAMES and (
        is_under(path, BOOK_DIR) or path.parent == BOOK_DIR
    ):
        return "structural"

    if is_under(path, BOOK_DIR / "scripts"):
        if any(name == prefix or name.startswith(prefix) for prefix in STRUCTURAL_SCRIPT_PREFIXES):
            return "structural"
        return "structural"

    if is_under(path, TOPICS_DIR):
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
            return "content"
        if not is_safe_md(path):
            # Non-md under topics (or unsafe name) → structural if new layout concern
            if path.suffix.lower() == ".md":
                return "structural"
            return "ignore"

        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            return "structural"  # deleted
        if rel not in cached_titles:
            return "structural"  # new file
        if current_titles.get(rel, "") != cached_titles.get(rel, ""):
            return "structural"  # H1 renamed
        return "content"

    return "ignore"


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=str(cwd or BOOK_DIR), check=True)


def full_build(reason: str) -> int:
    print(f"Structural change ({reason}); running full ./build.sh", flush=True)
    run(["./build.sh"], cwd=BOOK_DIR)
    save_title_cache(list_topic_markdown())
    return 0


def bookdown_generated_rel_paths() -> list[str]:
    if not BOOKDOWN_YML.is_file():
        return []
    paths: list[str] = []
    for line in BOOKDOWN_YML.read_text(encoding="utf-8").splitlines():
        match = re.search(r'"(\.\./_BOOK/generated/[^"]+\.md)"', line)
        if match:
            paths.append(match.group(1))
    return paths


def topic_to_generated_rel(topic_md: Path) -> str | None:
    """Map _TOPICS/Folder/File.md → ../_BOOK/generated/Folder/File.md if listed."""
    if not is_under(topic_md, TOPICS_DIR):
        return None
    rel_inside = topic_md.relative_to(TOPICS_DIR).as_posix()
    needle = f"../_BOOK/generated/{rel_inside}"
    listed = bookdown_generated_rel_paths()
    if needle in listed:
        return needle
    # Synthesized main page may exist only in generated/
    folder = topic_md.parent.name
    main_needle = f"../_BOOK/generated/{folder}/{folder}.md"
    if topic_md.name == f"{folder}.md" and main_needle in listed:
        return main_needle
    return None


def strip_html_text(fragment: str) -> str:
    text = TAG_RE.sub(" ", fragment)
    text = html_lib.unescape(text)
    text = WS_RE.sub(" ", text).strip()
    return text


def extract_search_entries_from_html(html_path: Path) -> list[dict[str, str]]:
    """Best-effort search entries for one rendered chapter (path + sections)."""
    raw = html_path.read_text(encoding="utf-8", errors="ignore")
    title_match = TITLE_RE.search(raw[:4000])
    if not title_match:
        return []
    chapter_num = title_match.group(1)
    chapter_title = html_lib.unescape(title_match.group(2)).strip()
    chapter_label = f"{chapter_num} {chapter_title}"

    main_match = re.search(
        r'<main[^>]*id="content"[^>]*>(.*)</main>',
        raw,
        re.IGNORECASE | re.DOTALL,
    )
    body = main_match.group(1) if main_match else raw

    # Split on section divs.
    parts = SECTION_RE.split(body)
    # parts: [preamble, id1, level1, content1, id2, level2, content2, ...]
    entries: list[dict[str, str]] = []
    if len(parts) < 4:
        text = strip_html_text(body)
        entries.append(
            {
                "path": html_path.name,
                "id": html_path.stem,
                "chapter": chapter_label,
                "heading": chapter_label,
                "text": text[:5000],
                "code": "",
            }
        )
        return entries

    # Preamble before first section often empty after classic layout; skip.
    i = 1
    while i + 2 < len(parts):
        sec_id = parts[i]
        level = parts[i + 1]
        content = parts[i + 2]
        i += 3
        # Heading text: first h1-h6 in content
        heading_match = re.search(
            r"<h[1-6][^>]*>(.*?)</h[1-6]>",
            content,
            re.IGNORECASE | re.DOTALL,
        )
        heading = (
            strip_html_text(heading_match.group(1))
            if heading_match
            else chapter_title
        )
        # Drop section number span noise already stripped by strip_html_text.
        text = strip_html_text(content)
        # Remove heading prefix from text once.
        if heading and text.startswith(heading):
            text = text[len(heading) :].strip()
        entries.append(
            {
                "path": html_path.name,
                "id": sec_id,
                "chapter": chapter_label,
                "heading": heading if level != "1" else chapter_label,
                "text": text[:5000],
                "code": "",
            }
        )
    return entries


def rebuild_search_json() -> int:
    """Rebuild search.json from every rendered chapter HTML page."""
    entries: list[dict] = []
    for path in sorted(BOOK_OUT.glob("*.html")):
        if path.name in {"404.html"}:
            continue
        entries.extend(extract_search_entries_from_html(path))
    SEARCH_JSON.write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")
    print(f"Rebuilt search.json ({len(entries)} entries).", flush=True)
    return len(entries)


def patch_search_json(html_names: list[str]) -> None:
    if not SEARCH_JSON.is_file():
        # preview_chapter / a wiped _book can leave HTML without search.json.
        rebuild_search_json()
        return

    data = json.loads(SEARCH_JSON.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise RuntimeError("search.json is not a list")

    keep = [entry for entry in data if entry.get("path") not in set(html_names)]
    added = 0
    for name in html_names:
        path = BOOK_OUT / name
        if not path.is_file():
            print(f"warning: cannot patch search for missing {name}", flush=True)
            continue
        entries = extract_search_entries_from_html(path)
        keep.extend(entries)
        added += len(entries)

    SEARCH_JSON.write_text(json.dumps(keep, ensure_ascii=False), encoding="utf-8")
    print(f"Patched search.json for {len(html_names)} page(s) ({added} entries).", flush=True)


def assign_chapter_hrefs(titles: list[str]) -> list[str]:
    """Match bookdown's slug collision scheme: foo.html, foo-1.html, foo-2.html, ..."""
    counts: dict[str, int] = {"index": 1}
    hrefs: list[str] = []
    for index, title in enumerate(titles):
        if index == 0:
            hrefs.append("index.html")
            continue
        base = slugify_text(title)
        n = counts.get(base, 0)
        counts[base] = n + 1
        hrefs.append(f"{base}.html" if n == 0 else f"{base}-{n}.html")
    return hrefs


def chapter_href_by_generated_rel() -> dict[str, str]:
    """Map each generated md path to its collision-aware HTML filename."""
    listed = bookdown_generated_rel_paths()
    titles = ["Introduction"]
    for rel in listed:
        titles.append(extract_title(resolve_generated_md(rel)))
    hrefs = assign_chapter_hrefs(titles)
    return {rel: hrefs[index + 1] for index, rel in enumerate(listed)}


def expected_chapter_number(generated_rel: str) -> int | None:
    listed = bookdown_generated_rel_paths()
    try:
        return listed.index(generated_rel) + 2
    except ValueError:
        return None


def _slug_family_names(base: str) -> list[Path]:
    """Return base.html / base-N.html paths that exist in the book output."""
    paths: list[Path] = []
    primary = BOOK_OUT / f"{base}.html"
    if primary.is_file():
        paths.append(primary)
    for path in sorted(BOOK_OUT.glob(f"{base}-*.html")):
        if re.fullmatch(rf"{re.escape(base)}-\d+\.html", path.name):
            paths.append(path)
    return paths


def href_for_generated_md(generated_rel: str) -> str | None:
    """
    Find rendered HTML for a generated md using bookdown title-collision hrefs.

    Never use bare slug matching alone: duplicate titles (e.g. topic + Notes
    both named Electromagnetism) must resolve to electromagnetism.html vs
    electromagnetism-1.html, not the same file.
    """
    mapping = chapter_href_by_generated_rel()
    expected = mapping.get(generated_rel)
    if expected and (BOOK_OUT / expected).is_file():
        return expected

    chapter_num = expected_chapter_number(generated_rel)
    if chapter_num is None:
        return expected

    try:
        md = resolve_generated_md(generated_rel)
    except RuntimeError:
        return expected

    base = slugify_text(extract_title(md))
    claimed = {href for rel, href in mapping.items() if rel != generated_rel}
    for path in _slug_family_names(base):
        if path.name in claimed:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")[:4000]
        match = TITLE_RE.search(text)
        if match and int(match.group(1)) == chapter_num:
            return path.name

    return expected


def missing_rendered_chapters() -> list[str]:
    """Listed generated chapters that have no matching HTML yet."""
    missing: list[str] = []
    for rel in bookdown_generated_rel_paths():
        href = href_for_generated_md(rel)
        if href is None or not (BOOK_OUT / href).is_file():
            missing.append(rel)
    return missing


def _close_div_offset(html: str, start: int) -> int:
    """Return index just past the matching </div> for the div that starts at start."""
    if not html.startswith("<div", start):
        raise RuntimeError("expected <div at section start")
    depth = 0
    i = start
    while i < len(html):
        next_open = html.find("<div", i)
        next_close = html.find("</div>", i)
        if next_close < 0:
            raise RuntimeError("unclosed section div")
        if next_open >= 0 and next_open < next_close:
            depth += 1
            i = next_open + 4
            continue
        depth -= 1
        i = next_close + len("</div>")
        if depth == 0:
            return i
    raise RuntimeError("unclosed section div")


def _decorate_pandoc_section(fragment: str, chapter_num: int) -> str:
    """Add bookdown-like section numbers / anchors to a pandoc section-divs fragment."""
    counters = [chapter_num]

    def next_number(level: int) -> str:
        nonlocal counters
        if level <= 1:
            counters = [chapter_num]
            return str(chapter_num)
        if len(counters) < level:
            counters = counters + [0] * (level - len(counters))
        else:
            counters = counters[:level]
        counters[level - 1] += 1
        return ".".join(str(n) for n in counters)

    out: list[str] = []
    pos = 0
    for match in re.finditer(
        r'<div\s+id="([^"]+)"\s+class="section level(\d+)"[^>]*>\s*'
        r"<h(\d)>(.*?)</h\3>",
        fragment,
        re.IGNORECASE | re.DOTALL,
    ):
        level = int(match.group(2))
        heading_level = int(match.group(3))
        sec_id = match.group(1)
        heading_inner = match.group(4).strip()
        number = next_number(level)
        out.append(fragment[pos : match.start()])
        out.append(
            f'<div id="{sec_id}" class="section level{level}" number="{number}">\n'
            f"<h{heading_level}>\n"
            f'<span class="header-section-number">{number}</span> {heading_inner}'
            f'<a class="anchor" aria-label="anchor" href="#{sec_id}">'
            f'<i class="fas fa-link"></i></a>\n'
            f"</h{heading_level}>"
        )
        pos = match.end()
    out.append(fragment[pos:])
    return "".join(out)


def pandoc_chapter_fragment(generated_md: Path) -> str:
    result = subprocess.run(
        [
            "pandoc",
            str(generated_md),
            "-f",
            "markdown+autolink_bare_uris+tex_math_single_backslash",
            "-t",
            "html4",
            "--section-divs",
            "--mathjax",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def first_paragraph_text(fragment: str) -> str:
    match = re.search(r"<p>(.*?)</p>", fragment, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return strip_html_text(match.group(1))


def resolve_generated_md(generated_rel: str) -> Path:
    if generated_rel.startswith("../_BOOK/"):
        path = BOOK_DIR / generated_rel[len("../_BOOK/") :]
    else:
        path = BOOK_DIR / generated_rel
    path = path.resolve()
    if not path.is_file():
        raise RuntimeError(f"Missing generated markdown: {generated_rel}")
    return path


def render_chapter_inplace(generated_rel: str, html_name: str) -> None:
    """
    Replace the level-1 section body inside an existing chapter HTML.

    bookdown::preview_chapter does not update per-chapter HTML in this merged
    TOPICS.Rmd / bs4_book setup (it only refreshes index.html), so we splice a
    pandoc render into the existing page shell.
    """
    html_path = BOOK_OUT / html_name
    if not html_path.is_file():
        raise RuntimeError(f"Missing chapter HTML for inplace render: {html_name}")

    generated_md = resolve_generated_md(generated_rel)
    existing = html_path.read_text(encoding="utf-8")
    title_match = TITLE_RE.search(existing[:4000])
    if not title_match:
        raise RuntimeError(f"Cannot read chapter number from {html_name}")
    # Prefer current bookdown order; fall back to the shell's stale number.
    chapter_num = expected_chapter_number(generated_rel) or int(title_match.group(1))
    page_title = extract_title(generated_md)

    fragment = pandoc_chapter_fragment(generated_md)
    fragment = _decorate_pandoc_section(fragment, chapter_num)

    sec_match = re.search(
        r'<div\s+id="[^"]+"\s+class="section level1"[^>]*>',
        existing,
    )
    if not sec_match:
        raise RuntimeError(f"No level-1 section in {html_name}")
    sec_end = _close_div_offset(existing, sec_match.start())
    updated = existing[: sec_match.start()] + fragment.rstrip() + "\n" + existing[sec_end:]

    # Refresh meta descriptions from the new lead paragraph.
    blurb = first_paragraph_text(fragment)
    if blurb:
        short = blurb if len(blurb) < 160 else blurb[:157].rstrip() + "..."
        escaped = html_lib.escape(short, quote=True)
        updated = re.sub(
            r'(<meta name="description" content=")(.*?)(">)',
            rf"\1{escaped}\3",
            updated,
            count=1,
            flags=re.DOTALL,
        )
        updated = re.sub(
            r'(<meta property="og:description" content=")(.*?)(">)',
            rf"\1{escaped}\3",
            updated,
            count=1,
            flags=re.DOTALL,
        )
        updated = re.sub(
            r'(<meta name="twitter:description" content=")(.*?)(">)',
            rf"\1{escaped}\3",
            updated,
            count=1,
            flags=re.DOTALL,
        )

    updated = re.sub(
        r"<title>.*?</title>",
        f"<title>{chapter_num} {html_lib.escape(page_title)} | Mathematics for Physics</title>",
        updated,
        count=1,
        flags=re.DOTALL,
    )

    html_path.write_text(updated, encoding="utf-8")
    print(f"Updated {html_name} in place from {generated_rel}", flush=True)


def content_build(topic_paths: list[Path], asset_only: bool) -> int:
    run(["python3", "scripts/generate_topics.py"], cwd=BOOK_DIR)

    missing = missing_rendered_chapters()
    if missing:
        sample = ", ".join(Path(rel).name for rel in missing[:5])
        return full_build(
            f"{len(missing)} chapter(s) listed but not rendered yet ({sample})"
        )

    generated_rels: list[str] = []
    for path in topic_paths:
        rel = topic_to_generated_rel(path)
        if rel is None:
            print(
                f"warning: {path} not in _bookdown.yml after generate; full build",
                flush=True,
            )
            return full_build(f"unlisted after generate: {path.name}")
        generated_rels.append(rel)

    if not asset_only and generated_rels:
        # Deduplicate while preserving order.
        unique: list[str] = []
        seen: set[str] = set()
        for rel in generated_rels:
            if rel not in seen:
                unique.append(rel)
                seen.add(rel)

        html_names: list[str] = []
        for rel in unique:
            href = href_for_generated_md(rel)
            if href is None or not (BOOK_OUT / href).is_file():
                return full_build(f"missing HTML for {rel}")
            html_names.append(href)

        if len(html_names) != len(set(html_names)):
            return full_build(
                "duplicate HTML targets for changed chapters "
                f"({', '.join(html_names)}); slug collision needs a full build"
            )

        for rel, href in zip(unique, html_names):
            render_chapter_inplace(rel, href)

        run(["python3", "scripts/filter_sidebar.py"], cwd=BOOK_DIR)
        run(["python3", "scripts/copy_topic_assets.py"], cwd=BOOK_DIR)

        # Search must exist before coverage checks (full bookdown creates it).
        patch_search_json(html_names)

        # Site Index + coverage (also rebuilds index links).
        run(["python3", "scripts/verify_book_coverage.py"], cwd=BOOK_DIR)

        # Ensure changed pages remain searchable.
        search_paths = {
            entry.get("path")
            for entry in json.loads(SEARCH_JSON.read_text(encoding="utf-8"))
            if isinstance(entry, dict)
        }
        missing = [name for name in html_names if name not in search_paths]
        if missing:
            raise RuntimeError(
                "Changed pages missing from search.json after patch: "
                + ", ".join(missing)
                + ". Run ./build.sh"
            )

        # Verify HTML body actually contains fresh generated lead text.
        for rel, href in zip(unique, html_names):
            gen_path = BOOK_DIR / rel[len("../_BOOK/") :] if rel.startswith("../_BOOK/") else BOOK_DIR / rel
            if not gen_path.is_file():
                gen_path = (BOOK_DIR / "generated" / Path(rel).parts[-2] / Path(rel).name)
            lead = first_paragraph_text(pandoc_chapter_fragment(gen_path))
            html_text = (BOOK_OUT / href).read_text(encoding="utf-8", errors="ignore")
            if lead and lead[:60] not in strip_html_text(html_text):
                raise RuntimeError(
                    f"{href} does not contain updated content from {rel}. "
                    "Run ./build.sh"
                )

        print(f"Incremental build OK: {', '.join(html_names)}", flush=True)
    else:
        run(["python3", "scripts/copy_topic_assets.py"], cwd=BOOK_DIR)
        print("Assets copied (no markdown preview).", flush=True)

    save_title_cache(list_topic_markdown())
    return 0


def seed_cache() -> int:
    titles = list_topic_markdown()
    save_title_cache(titles)
    print(f"Seeded title cache with {len(titles)} topic pages.", flush=True)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--seed-cache",
        action="store_true",
        help="Write .watch-titles.json from current _TOPICS H1s and exit",
    )
    parser.add_argument(
        "--changed",
        nargs="*",
        default=[],
        help="Paths reported by the file watcher",
    )
    args = parser.parse_args(argv)

    if args.seed_cache:
        return seed_cache()

    if not args.changed:
        print("error: pass --changed paths or --seed-cache", file=sys.stderr)
        return 2

    if not BOOK_OUT.is_dir() or not (BOOK_OUT / "index.html").is_file():
        return full_build("missing _book output")

    cached = load_title_cache()
    if not cached:
        # First watch session without cache: seed then treat as content if possible.
        cached = list_topic_markdown()
        save_title_cache(cached)

    current = list_topic_markdown()

    # Detect deletions even if watcher only sent the path.
    cached_keys = set(cached)
    current_keys = set(current)
    if cached_keys - current_keys:
        deleted = sorted(cached_keys - current_keys)
        return full_build(f"deleted topic files: {', '.join(deleted[:5])}")
    if current_keys - cached_keys:
        added = sorted(current_keys - cached_keys)
        # Only force full build if an added file is among --changed or any new file exists
        return full_build(f"new topic files: {', '.join(added[:5])}")

    kinds: list[str] = []
    content_md: list[Path] = []
    asset_paths: list[Path] = []
    reasons: list[str] = []

    for raw in args.changed:
        path = resolve_changed(raw)
        if path is None:
            continue
        kind = classify_change(path, cached, current)
        if kind == "ignore":
            continue
        kinds.append(kind)
        if kind == "structural":
            reasons.append(path.name)
        elif is_under(path, TOPICS_DIR) and is_safe_md(path):
            content_md.append(path)
        elif is_under(path, TOPICS_DIR):
            asset_paths.append(path)

    if not kinds:
        print("No relevant changes.", flush=True)
        return 0

    if "structural" in kinds:
        return full_build(", ".join(reasons[:8]) or "structural")

    # Content-only
    return content_build(content_md, asset_only=bool(asset_paths) and not content_md)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"error: command failed with exit {exc.returncode}", file=sys.stderr)
        raise SystemExit(exc.returncode)
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)

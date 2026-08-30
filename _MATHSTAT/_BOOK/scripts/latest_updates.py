#!/usr/bin/env python3
"""Write latest-updates.json / .js and wire them into every book HTML page."""

from __future__ import annotations

import html as html_lib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BOOK_DIR.parent
GIT_ROOT = REPO_ROOT.parent
TOPICS_DIR = REPO_ROOT / "_TOPICS"
TOPICS_GIT_PATH = TOPICS_DIR.relative_to(GIT_ROOT).as_posix()
BOOK_OUT = BOOK_DIR / "_book"
BOOKDOWN_YML = BOOK_DIR / "_bookdown.yml"
JSON_NAME = "latest-updates.json"
JS_NAME = "latest-updates.js"
TOP_N = 5
SCRIPT_TAG = f'<script src="{JS_NAME}"></script>'
TITLE_RE = re.compile(
    r"<title>(\d+)\s+(.*?)\s+\|\s*[^<]*</title>",
    re.IGNORECASE | re.DOTALL,
)


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


def is_draft_md(path: Path) -> bool:
    return path.name.endswith(".draft.md") or path.name.endswith(".skip.md")


def is_safe_md(path: Path) -> bool:
    if is_draft_md(path):
        return False
    return path.suffix.lower() == ".md" and re.fullmatch(
        r"[A-Za-z0-9._-]+\.md", path.name
    )


def bookdown_generated_rel_paths() -> list[str]:
    if not BOOKDOWN_YML.is_file():
        return []
    paths: list[str] = []
    for line in BOOKDOWN_YML.read_text(encoding="utf-8").splitlines():
        match = re.search(r'"(\.\./_BOOK/generated/[^"]+\.md)"', line)
        if match:
            paths.append(match.group(1))
    return paths


def format_date(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%d/%m/%Y")


def git_topic_timestamps() -> dict[str, float]:
    """Map repo-relative topic paths → most recent commit unix time."""
    result = subprocess.run(
        [
            "git",
            "log",
            "--pretty=format:COMMIT %ct",
            "--name-only",
            "--",
            TOPICS_GIT_PATH,
        ],
        cwd=GIT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return {}

    timestamps: dict[str, float] = {}
    current_ts: float | None = None
    for line in result.stdout.splitlines():
        if line.startswith("COMMIT "):
            try:
                current_ts = float(line.split()[1])
            except (IndexError, ValueError):
                current_ts = None
            continue
        if not line.endswith(".md") or current_ts is None:
            continue
        rel = Path(line)
        try:
            key = rel.relative_to(REPO_ROOT.name).as_posix()
        except ValueError:
            key = line
        if key not in timestamps:
            timestamps[key] = current_ts
    return timestamps


def git_dirty_topics() -> set[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--", TOPICS_GIT_PATH],
        cwd=GIT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    dirty: set[str] = set()
    if result.returncode != 0:
        return dirty
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1].strip()
        rel = Path(path)
        try:
            path = rel.relative_to(REPO_ROOT.name).as_posix()
        except ValueError:
            path = rel.as_posix()
        if path.endswith(".md"):
            dirty.add(path)
    return dirty


def update_stamp(
    path: Path,
    *,
    git_ts_map: dict[str, float],
    dirty: set[str],
) -> tuple[float, str]:
    """Prefer git history; use mtime for dirty / untracked local edits."""
    rel = path.relative_to(REPO_ROOT).as_posix()
    mtime = path.stat().st_mtime
    if rel in dirty or rel not in git_ts_map:
        return mtime, format_date(mtime)
    git_ts = git_ts_map[rel]
    return git_ts, format_date(git_ts)


def topic_source_for_generated(rel: str) -> Path | None:
    # ../_BOOK/generated/Folder/File.md → _TOPICS/Folder/File.md
    if not rel.startswith("../_BOOK/generated/"):
        return None
    inner = rel[len("../_BOOK/generated/") :]
    topic = TOPICS_DIR / inner
    if topic.is_file():
        return topic
    return None


def chapter_href_map() -> dict[str, str]:
    """Map generated rel → existing HTML, using title collisions + live files."""
    sys.path.insert(0, str(BOOK_DIR / "scripts"))
    try:
        import incremental_build as ib  # type: ignore

        mapping = ib.chapter_href_by_generated_rel()
        resolved: dict[str, str] = {}
        # Resolve once per rel without rebuilding the collision map each time.
        claimed = set(mapping.values())
        for rel, expected in mapping.items():
            if (BOOK_OUT / expected).is_file():
                resolved[rel] = expected
                continue
            chapter_num = ib.expected_chapter_number(rel)
            if chapter_num is None:
                continue
            try:
                md = ib.resolve_generated_md(rel)
            except RuntimeError:
                continue
            base = ib.slugify_text(ib.extract_title(md))
            for path in ib._slug_family_names(base):
                if path.name in claimed and path.name != expected:
                    continue
                text = path.read_text(encoding="utf-8", errors="ignore")[:4000]
                match = TITLE_RE.search(text)
                if match and int(match.group(1)) == chapter_num:
                    resolved[rel] = path.name
                    break
        return resolved
    except Exception:
        pass

    # Fallback: match by chapter number in rendered titles.
    rendered: dict[int, str] = {}
    for path in BOOK_OUT.glob("*.html"):
        if path.name in {"404.html"}:
            continue
        match = TITLE_RE.search(path.read_text(encoding="utf-8", errors="ignore")[:4000])
        if match:
            rendered[int(match.group(1))] = path.name

    out: dict[str, str] = {}
    for index, rel in enumerate(bookdown_generated_rel_paths(), start=2):
        href = rendered.get(index)
        if href:
            out[rel] = href
    return out


def collect_updates(limit: int = TOP_N) -> list[dict[str, str]]:
    href_map = chapter_href_map()
    git_ts_map = git_topic_timestamps()
    dirty = git_dirty_topics()
    rows: list[tuple[float, dict[str, str]]] = []
    seen_href: set[str] = set()

    for rel in bookdown_generated_rel_paths():
        source = topic_source_for_generated(rel)
        if source is None or not is_safe_md(source):
            continue
        href = href_map.get(rel)
        if not href or href in seen_href:
            continue
        if not (BOOK_OUT / href).is_file():
            continue
        ts, date = update_stamp(source, git_ts_map=git_ts_map, dirty=dirty)
        rows.append(
            (
                ts,
                {
                    "title": extract_title(source),
                    "href": href,
                    "date": date,
                },
            )
        )
        seen_href.add(href)

    rows.sort(key=lambda item: item[0], reverse=True)
    return [item for _, item in rows[:limit]]


def write_js() -> None:
    # Escape-safe client filler for the classic site footer.
    js = r"""(function () {
  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function ensureList(footer) {
    var block = footer.querySelector(".latest-updates");
    if (!block) {
      block = document.createElement("div");
      block.className = "latest-updates";
      block.innerHTML =
        '<h2 class="latest-updates-title">Latest Updates</h2>' +
        '<ul class="latest-updates-list"></ul>';
      footer.insertBefore(block, footer.firstChild);
    }
    return block.querySelector(".latest-updates-list");
  }

  function fill(list, items) {
    if (!list || list.getAttribute("data-loaded") === "1") return;
    if (!items || !items.length) {
      list.closest(".latest-updates").style.display = "none";
      return;
    }
    list.innerHTML = items
      .map(function (item) {
        return (
          "<li>" +
          '<a href="' +
          escapeHtml(item.href) +
          '">' +
          escapeHtml(item.title) +
          "</a>" +
          '<span class="latest-updates-date">' +
          escapeHtml(item.date) +
          "</span>" +
          "</li>"
        );
      })
      .join("");
    list.setAttribute("data-loaded", "1");
  }

  function run() {
    var footer = document.querySelector("#colophon.site-footer, footer.site-footer");
    if (!footer) return false;
    var list = ensureList(footer);
    if (!list) return false;
    if (list.getAttribute("data-loaded") === "1") return true;
    fetch("latest-updates.json", { cache: "no-store" })
      .then(function (response) {
        return response.ok ? response.json() : [];
      })
      .then(function (items) {
        fill(list, items);
      })
      .catch(function () {
        var block = footer.querySelector(".latest-updates");
        if (block) block.style.display = "none";
      });
    return true;
  }

  function start() {
    if (run()) return;
    var tries = 0;
    var timer = setInterval(function () {
      tries += 1;
      if (run() || tries > 40) clearInterval(timer);
    }, 50);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
"""
    (BOOK_OUT / JS_NAME).write_text(js, encoding="utf-8")


def inject_script_tags() -> int:
    if not BOOK_OUT.is_dir():
        return 0
    updated = 0
    for path in BOOK_OUT.glob("*.html"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SCRIPT_TAG in text:
            continue
        if "</body>" not in text.lower():
            continue
        # Case-preserving replace of the closing body tag.
        match = re.search(r"</body>", text, flags=re.IGNORECASE)
        if not match:
            continue
        text = text[: match.start()] + SCRIPT_TAG + "\n" + text[match.start() :]
        path.write_text(text, encoding="utf-8")
        updated += 1
    return updated


def main() -> None:
    BOOK_OUT.mkdir(parents=True, exist_ok=True)
    updates = collect_updates(TOP_N)
    (BOOK_OUT / JSON_NAME).write_text(
        json.dumps(updates, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_js()
    injected = inject_script_tags()
    labels = ", ".join(f"{u['title']} ({u['date']})" for u in updates) or "none"
    print(
        f"Wrote {JSON_NAME} with {len(updates)} update(s): {labels}. "
        f"Injected script into {injected} page(s).",
        flush=True,
    )


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

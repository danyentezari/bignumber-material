#!/usr/bin/env bash
# Watch topic sources and book chrome; incrementally rebuild changed chapters.
# Structural edits (new/deleted pages, H1 renames, sidebar/chrome) trigger a
# full ./build.sh. Content edits use bookdown::preview_chapter and refresh
# Site Index, sidebar navigation, and search.json.
#
# Usage: ./_BOOK/watch-build.sh
# Stop:  Ctrl-C
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v fswatch >/dev/null 2>&1; then
  echo "error: fswatch not found. Install with: brew install fswatch" >&2
  exit 1
fi

if [[ ! -d _book || ! -f _book/index.html ]]; then
  echo "No book output yet; running full build first..."
  ./build.sh
fi

python3 scripts/incremental_build.py --seed-cache

echo "Watching _TOPICS and book chrome (Ctrl-C to stop)..."
echo "Content edits → incremental preview; structural edits → full build."

# Debounce: collect paths until 1s quiet, then rebuild once.
fswatch -r \
  --event Created \
  --event Updated \
  --event Removed \
  --event Renamed \
  --latency 0.2 \
  ../_TOPICS \
  sidebar.txt \
  index.Rmd \
  head.html \
  after_body.html \
  style.css \
  scripts \
  _output.yml \
  published.txt \
| {
  changed=()
  while true; do
    if IFS= read -r -t 1 path; then
      # Skip noise and output dirs if they appear.
      case "$path" in
        */_book/*|*/generated/*|*/.DS_Store|*~) continue ;;
      esac
      changed+=("$path")
    else
      # Timeout with no new events.
      if ((${#changed[@]} > 0)); then
        echo ""
        echo "---- $(date '+%H:%M:%S') changes: ${#changed[@]} path(s) ----"
        python3 scripts/incremental_build.py --changed "${changed[@]}" || {
          echo "Incremental build failed; fix errors or run ./build.sh" >&2
        }
        changed=()
      fi
    fi
  done
}

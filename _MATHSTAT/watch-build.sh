#!/usr/bin/env bash
# Watch topic sources and book chrome. On change: regenerate main.tex from
# _TOPICS, rebuild main.pdf, and incrementally rebuild the HTML book.
#
# Usage: ./watch-build.sh
# Stop:  Ctrl-C
set -euo pipefail
cd "$(dirname "$0")"

export PATH="${HOME}/Library/TinyTeX/bin/universal-darwin:${PATH}"

if ! command -v fswatch >/dev/null 2>&1; then
  echo "error: fswatch not found. Install with: brew install fswatch" >&2
  exit 1
fi

if ! command -v latexmk >/dev/null 2>&1; then
  echo "error: latexmk not found. Expected TinyTeX at ~/Library/TinyTeX/bin/universal-darwin" >&2
  exit 1
fi

rebuild_tex_pdf() {
  python3 _BOOK/scripts/export_to_tex.py
  latexmk -pdf -interaction=nonstopmode -file-line-error -synctex=1 main.tex
}

if [[ ! -d _BOOK/_book || ! -f _BOOK/_book/index.html ]]; then
  echo "No book output yet; running full build first..."
  ./_BOOK/build.sh
fi

python3 _BOOK/scripts/incremental_build.py --seed-cache

# Catch topics added while the watcher was stopped (seed alone would hide them).
python3 _BOOK/scripts/generate_topics.py >/dev/null
if ! python3 -c "
import sys
from pathlib import Path
sys.path.insert(0, '_BOOK/scripts')
from incremental_build import missing_rendered_chapters
missing = missing_rendered_chapters()
if missing:
    print('Missing rendered HTML for: ' + ', '.join(Path(m).name for m in missing[:8]))
    raise SystemExit(1)
"; then
  echo "Book HTML is behind _TOPICS; running full build..."
  ./_BOOK/build.sh
  python3 _BOOK/scripts/incremental_build.py --seed-cache
fi

echo "Syncing main.tex and main.pdf from _TOPICS..."
rebuild_tex_pdf || {
  echo "PDF rebuild failed; watching anyway (fix errors in _TOPICS or LaTeX)" >&2
}

echo "Watching _TOPICS and book chrome (Ctrl-C to stop)..."
echo "Each change regenerates main.tex, rebuilds the PDF, then updates HTML."
echo "Content edits → incremental HTML; structural edits → full book build."

watch_paths=(
  _TOPICS
  _BOOK/sidebar.txt
  _BOOK/structure.txt
  _BOOK/index.Rmd
  _BOOK/head.html
  _BOOK/after_body.html
  _BOOK/style.css
  _BOOK/scripts
  _BOOK/_output.yml
  _BOOK/published.txt
)
if [[ -d images ]]; then
  watch_paths+=(images)
fi

# Debounce: collect paths until 1s quiet, then rebuild once.
fswatch -r \
  --event Created \
  --event Updated \
  --event Removed \
  --event Renamed \
  --latency 0.2 \
  "${watch_paths[@]}" \
| {
  changed=()
  while true; do
    if IFS= read -r -t 1 path; then
      case "$path" in
        */_book/*|*/generated/*|*/.DS_Store|*~) continue ;;
        *.pdf|*.aux|*.log|*.fls|*.fdb_latexmk|*.synctex.gz) continue ;;
        */main.tex) continue ;;
      esac
      changed+=("$path")
    else
      if ((${#changed[@]} > 0)); then
        echo ""
        echo "---- $(date '+%H:%M:%S') changes: ${#changed[@]} path(s) ----"
        rebuild_tex_pdf || {
          echo "PDF rebuild failed; fix errors in _TOPICS or LaTeX" >&2
        }
        (cd _BOOK && python3 scripts/incremental_build.py --changed "${changed[@]}") || {
          echo "Incremental HTML build failed; fix errors or run ./_BOOK/build.sh" >&2
        }
        changed=()
      fi
    fi
  done
}

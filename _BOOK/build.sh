#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Stale chapter HTML in _book/ makes bookdown pick electromagnetism-2.html etc.,
# so Site Index / search hrefs drift from the real files. Wipe top-level HTML first.
if [[ -d _book ]]; then
  find _book -maxdepth 1 -type f \( -name '*.html' -o -name 'search.json' -o -name 'reference-keys.txt' \) -delete
fi

Rscript -e 'source("pre-render.R"); bookdown::render_book("index.Rmd", "bookdown::bs4_book"); source("post-render.R")'

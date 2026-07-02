#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
Rscript -e 'source("pre-render.R"); bookdown::render_book("index.Rmd", "bookdown::bs4_book"); source("post-render.R")'

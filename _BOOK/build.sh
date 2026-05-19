#!/usr/bin/env sh

# Build the TOPICS Bookdown book from the _BOOK folder.
# Requires R and the bookdown package to be installed.

Rscript -e 'bookdown::render_book("index.Rmd", "bookdown::html_book")'

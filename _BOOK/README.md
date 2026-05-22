# TOPICS Book

This folder contains the Bookdown project for the `_TOPICS` content.

## Build

From `_BOOK`:

```sh
Rscript -e 'bookdown::render_book("index.Rmd", "bookdown::bs4_book")'
```

If `Rscript` is not available, install R and ensure it is on your shell `PATH`.

## Theme

This project now uses the built-in `bookdown::bs4_book` theme with Bootswatch `flatly`, plus custom serif font styling via `style.css`.

## Output

The rendered HTML book will be placed into `_BOOK/_book` by default.


## Run

cd './_BOOK/_book'

python3 -m http.server 8000


## Notes

- Source markdown files remain in `../_TOPICS`.
- The Bookdown order is defined in `_bookdown.yml`.


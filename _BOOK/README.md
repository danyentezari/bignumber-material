# TOPICS Book

## Quick Commands

```bash
# full build
./_BOOK/build.sh

# watch and rebuild on change (needs fswatch: brew install fswatch)
./_BOOK/watch-build.sh

# serve the book (from repo root after a build)
python3 -m http.server 8000 --directory _BOOK/_book
```

This folder contains the Bookdown project for the `_TOPICS` content.

## Build

From the repo root:

```sh
./_BOOK/build.sh
```

If `Rscript` is not available, install R and ensure it is on your shell `PATH`.

### Watch / incremental build

```sh
./_BOOK/watch-build.sh
```

Watches `_TOPICS` and book chrome. Content edits to existing pages rebuild only those chapters (plus Site Index, sidebar, and search). New/deleted pages, H1 renames, `sidebar.txt`, and chrome/script changes trigger a full build. Requires [fswatch](https://github.com/emcrisostomo/fswatch) (`brew install fswatch`).

## Theme

This project uses `bookdown::bs4_book` with a custom, MasterClass-inspired UI:

- **Serif typography** (Spectral) for a printed-book feel, with `JetBrains Mono` for code and STIX for math — defined in `style.css`.
- **Light/dark mode toggle** in the top-right corner. The choice is saved to `localStorage` and defaults to the OS color scheme.
- Theme plumbing lives in two includes wired through `_output.yml`:
  - `head.html` — loads fonts and applies the saved theme before first paint (no flash).
  - `after_body.html` — renders the toggle button and its logic.

Colors are driven by CSS variables on `[data-theme]`, so tweak the `:root` / `[data-theme="dark"]` blocks at the top of `style.css` to recolor the whole book.

## Output

The rendered HTML book will be placed into `_BOOK/_book` by default.


## Run

```bash
cd './_BOOK/_book'
python3 -m http.server 8000
```

Or, without cd'ing into `_book`:

```bash
python3 -m http.server 8000 --directory _BOOK/_book
```


## Notes

- Source markdown files remain in `../_TOPICS`.

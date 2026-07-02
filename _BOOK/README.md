# TOPICS Book

This folder contains the Bookdown project for the `_TOPICS` content.

## Build

From `_BOOK`:

```sh
./_BOOK/build.sh
```

If `Rscript` is not available, install R and ensure it is on your shell `PATH`.

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
python3 -m http.server 8000 --directory _book
```


## Notes

- Source markdown files remain in `../_TOPICS`.

# TOPICS Book

## Quick Commands

```bash
# serve the book (from repo root after a build)
python3 -m http.server 8000 --directory _BOOK/_book

# full build
./_BOOK/build.sh

# watch and rebuild on changes
./_BOOK/watch-build.sh
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

Post-render also writes SEO files into `_BOOK/_book`:

- `robots.txt` — allows crawling and points at the sitemap
- `sitemap.xml` — absolute HTTPS URLs for every chapter
- `CNAME` — `book.danyentezari.com`
- `rel=canonical` and `og:url` on each HTML page

## SEO / Google indexing

After deploying to GitHub Pages:

1. In the repo **Settings → Pages**, enable **Enforce HTTPS** for `book.danyentezari.com`. Confirm `http://book.danyentezari.com` redirects to `https://`, and that `https://danyentezari.github.io/bignumber-material/` redirects to the HTTPS custom domain.
2. In [Google Search Console](https://search.google.com/search-console), add a Domain property for `book.danyentezari.com` (DNS TXT) or a URL-prefix property and verify.
3. Submit the sitemap: `https://book.danyentezari.com/sitemap.xml`.
4. Use URL Inspection on the home page, Site Index, and one deep chapter; watch Coverage for soft-404s or http/https duplicates.

Optional: submit the same sitemap in Bing Webmaster Tools.

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
- Topic drafts named `*.draft.md` are excluded from the book.
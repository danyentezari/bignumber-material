status <- system("python3 scripts/filter_sidebar.py")
if (!identical(status, 0L)) {
  stop("filter_sidebar.py failed", call. = FALSE)
}

status <- system("python3 scripts/copy_topic_assets.py")
if (!identical(status, 0L)) {
  stop("copy_topic_assets.py failed", call. = FALSE)
}

status <- system("python3 scripts/verify_book_coverage.py")
if (!identical(status, 0L)) {
  stop("verify_book_coverage.py failed", call. = FALSE)
}

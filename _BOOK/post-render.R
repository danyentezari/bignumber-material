status <- system("python3 scripts/filter_sidebar.py")
if (!identical(status, 0L)) {
  stop("filter_sidebar.py failed", call. = FALSE)
}

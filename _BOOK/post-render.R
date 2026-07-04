status <- system("python3 scripts/filter_sidebar.py")
if (!identical(status, 0L)) {
  stop("filter_sidebar.py failed", call. = FALSE)
}

status <- system("python3 scripts/copy_topic_assets.py")
if (!identical(status, 0L)) {
  stop("copy_topic_assets.py failed", call. = FALSE)
}

status <- system("python3 scripts/generate_topics.py")
if (!identical(status, 0L)) {
  stop("generate_topics.py failed", call. = FALSE)
}

(function () {
  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function ensureList(footer) {
    var block = footer.querySelector(".latest-updates");
    if (!block) {
      block = document.createElement("div");
      block.className = "latest-updates";
      block.innerHTML =
        '<h2 class="latest-updates-title">Latest Updates</h2>' +
        '<ul class="latest-updates-list"></ul>';
      footer.insertBefore(block, footer.firstChild);
    }
    return block.querySelector(".latest-updates-list");
  }

  function fill(list, items) {
    if (!list || list.getAttribute("data-loaded") === "1") return;
    if (!items || !items.length) {
      list.closest(".latest-updates").style.display = "none";
      return;
    }
    list.innerHTML = items
      .map(function (item) {
        return (
          "<li>" +
          '<a href="' +
          escapeHtml(item.href) +
          '">' +
          escapeHtml(item.title) +
          "</a>" +
          '<span class="latest-updates-date">' +
          escapeHtml(item.date) +
          "</span>" +
          "</li>"
        );
      })
      .join("");
    list.setAttribute("data-loaded", "1");
  }

  function run() {
    var footer = document.querySelector("#colophon.site-footer, footer.site-footer");
    if (!footer) return false;
    var list = ensureList(footer);
    if (!list) return false;
    if (list.getAttribute("data-loaded") === "1") return true;
    fetch("latest-updates.json", { cache: "no-store" })
      .then(function (response) {
        return response.ok ? response.json() : [];
      })
      .then(function (items) {
        fill(list, items);
      })
      .catch(function () {
        var block = footer.querySelector(".latest-updates");
        if (block) block.style.display = "none";
      });
    return true;
  }

  function start() {
    if (run()) return;
    var tries = 0;
    var timer = setInterval(function () {
      tries += 1;
      if (run() || tries > 40) clearInterval(timer);
    }, 50);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();

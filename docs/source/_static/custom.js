console.log("custom.js loaded");

if (window.location.pathname.includes("/1-lab-overview/")) {
  document.body.classList.add("lab-overview-section");
}

document.addEventListener("DOMContentLoaded", function () {
  if (!window.location.pathname.includes("/1-lab-overview/")) return;

  document
    .querySelectorAll(
      ".wy-menu-vertical li.toctree-l1.current > ul > li.toctree-l2 > ul > li.toctree-l3 > ul"
    )
    .forEach(list => list.remove());

  if (document.body.classList.contains("lab-overview-page")) {
    document
      .querySelectorAll(
        ".rst-content section.sidebar-nav-group, .rst-content section#lab-operations, .rst-content section#research-and-resources"
      )
      .forEach(section => section.remove());
  }
});

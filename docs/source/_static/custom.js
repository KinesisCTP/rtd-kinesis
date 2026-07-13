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

// ===== APPLE-STYLE NAVBAR BEHAVIOR =====
document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".top-navbar");
  if (!navbar) return;

  function updateNavbar() {
    if (window.scrollY > 80) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  }

  updateNavbar();
  window.addEventListener("scroll", updateNavbar);

  const currentPath = window.location.pathname;

  document.querySelectorAll(".nav-links a").forEach(link => {
    const linkPath = new URL(link.href).pathname;

    if (
      currentPath === linkPath ||
      currentPath.includes(linkPath.replace("/index.html", "")) && linkPath !== "/"
    ) {
      link.classList.add("active");
    }
  });
});

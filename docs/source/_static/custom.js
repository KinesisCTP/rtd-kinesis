document.addEventListener("DOMContentLoaded", function () {
  if (!window.location.pathname.includes("/1-lab-overview/")) return;

  document.body.classList.add("lab-overview-section");

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

document.addEventListener("DOMContentLoaded", function () {
  const dialog = document.querySelector("[data-publication-intake-dialog]");
  const openButton = document.querySelector("[data-publication-intake-help]");
  const closeButton = document.querySelector("[data-publication-intake-close]");

  if (
    typeof HTMLDialogElement === "undefined" ||
    !(dialog instanceof HTMLDialogElement) ||
    !(openButton instanceof HTMLElement)
  ) {
    return;
  }

  const intake = openButton.closest(".publication-intake");
  if (intake instanceof HTMLElement) {
    intake.classList.add("publication-intake--dialog-ready");
  }

  openButton.addEventListener("click", function () {
    dialog.showModal();
  });

  if (closeButton instanceof HTMLElement) {
    closeButton.addEventListener("click", function () {
      dialog.close();
    });
  }

  dialog.addEventListener("click", function (event) {
    if (event.target === dialog) {
      dialog.close();
    }
  });
});

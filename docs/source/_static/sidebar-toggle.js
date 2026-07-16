(function () {
  function createMenuIcon() {
    return `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M4 7H20" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M4 12H20" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M4 17H20" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
    `;
  }

  function createCloseIcon() {
    return `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M6 6L18 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
    `;
  }

  document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.querySelector(".wy-nav-side");
    const content = document.querySelector(".wy-nav-content-wrap");
    if (!sidebar || !content) return;

    sidebar.id = sidebar.id || "wy-nav-side";

    let button = document.querySelector(".wy-nav-top .menu-toggle");
    if (!button) return;

    const cleanButton = button.cloneNode(true);
    button.replaceWith(cleanButton);
    button = cleanButton;

    button.type = "button";
    button.setAttribute("aria-controls", sidebar.id);

    function isWideEnoughForOpenSidebar() {
      return window.innerWidth >= 1180 && window.innerWidth / window.innerHeight >= 1.25;
    }

    function setSidebarOpen(isOpen) {
      const isMobile = window.matchMedia("(max-width: 850px)").matches;

      document.body.classList.toggle("sidebar-open", isOpen);
      document.body.classList.toggle("sidebar-closed", !isOpen);
      button.classList.toggle("sidebar-open", isOpen);
      button.classList.toggle("sidebar-closed", !isOpen);
      button.setAttribute("aria-expanded", String(isOpen));
      button.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
      button.innerHTML = `
        <span class="menu-toggle-icon">${isOpen ? createCloseIcon() : createMenuIcon()}</span>
        <span class="menu-toggle-label">${isOpen ? "Close" : "Contents"}</span>
      `;

      sidebar.classList.toggle("active", isMobile && isOpen);
      sidebar.classList.toggle("collapsed", !isOpen);
      content.classList.toggle("shifted", !isOpen);
    }

    let currentDefaultIsOpen = isWideEnoughForOpenSidebar();
    setSidebarOpen(currentDefaultIsOpen);

    button.addEventListener("click", function () {
      setSidebarOpen(!document.body.classList.contains("sidebar-open"));
    });

    window.addEventListener("resize", function () {
      const nextDefaultIsOpen = isWideEnoughForOpenSidebar();
      if (nextDefaultIsOpen !== currentDefaultIsOpen) {
        currentDefaultIsOpen = nextDefaultIsOpen;
        setSidebarOpen(nextDefaultIsOpen);
      }
    });
  });
})();

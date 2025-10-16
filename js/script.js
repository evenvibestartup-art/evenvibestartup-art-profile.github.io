// Toggle class active
const navbarNav = document.querySelector(".navbar-nav");

document.querySelector("#hamburger-menu").onclick = (e) => {
  navbarNav.classList.toggle("active");
  e.preventDefault();
};

// klik di luar side bar
const hamburgermenu = document.querySelector(".navbar-nav");
const hamburger = document.querySelector("#hamburger-menu");

document.addEventListener("click", function (e) {
  if (!hamburger.contains(e.target) && !navbarNav.contains(e.target)) {
    navbarNav.classList.remove("active");
  }
});

// Floating Menu
const menuToggle = document.querySelector("#floating-menu-toggle");
const menuPopup = document.querySelector(".floating-menu-popup");

menuToggle.onclick = () => {
  menuPopup.classList.toggle("active");

  const icon = menuToggle.querySelector("i");
  if (menuPopup.classList.contains("active")) {
    icon.setAttribute("data-feather", "x");
  } else {
    icon.setAttribute("data-feather", "menu");
  }
  feather.replace();
};

menuPopup.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    menuPopup.classList.remove("active");
    menuToggle.querySelector("i").setAttribute("data-feather", "menu");
    feather.replace();
  });
});

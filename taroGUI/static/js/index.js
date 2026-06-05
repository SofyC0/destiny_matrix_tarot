const burger = document.getElementById("burger");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

function toggleMenu() {

    burger.classList.toggle("active");
    sidebar.classList.toggle("active");
    overlay.classList.toggle("active");
}

burger.addEventListener("click", toggleMenu);

overlay.addEventListener("click", () => {

    burger.classList.remove("active");
    sidebar.classList.remove("active");
    overlay.classList.remove("active");

});
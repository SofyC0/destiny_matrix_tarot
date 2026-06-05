const burger = document.getElementById("burger");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

burger.addEventListener("click", () => {

    burger.classList.toggle("active");
    sidebar.classList.toggle("active");
    overlay.classList.toggle("active");

});

overlay.addEventListener("click", () => {

    burger.classList.remove("active");
    sidebar.classList.remove("active");
    overlay.classList.remove("active");

});

document.addEventListener("keydown", (event) => {

    if(event.key === "Escape"){

        burger.classList.remove("active");
        sidebar.classList.remove("active");
        overlay.classList.remove("active");

    }

});
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

    if (event.key === "Escape") {

        burger.classList.remove("active");
        sidebar.classList.remove("active");
        overlay.classList.remove("active");

    }

});

const modal = document.getElementById("modalOverlay");
const closeModal = document.getElementById("closeModal");

const detailsBtn = document.querySelector(".card-of-day button");

detailsBtn.addEventListener("click", () => {
    modal.classList.add("active");
});

closeModal.addEventListener("click", () => {
    modal.classList.remove("active");
});

modal.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.classList.remove("active");
    }
});

const spreadModal = document.getElementById("spreadModal");
const spreadClose = document.getElementById("spreadClose");

const spreadTitle = document.getElementById("spreadTitle");
const spreadDescription = document.getElementById("spreadDescription");

const spreadButtons = document.querySelectorAll(".spread-btn");
let selectedCardsCount = 1;
const startSpreadButtons =
    document.querySelectorAll(".startSpread");
let currentSpreadType = "";

startSpreadButtons.forEach(button => {

    button.addEventListener("click", () => {

        const question = document.querySelector(
            ".question textarea"
        ).value;

        localStorage.setItem(
            "spreadTitle",
            spreadTitle.textContent
        );

        localStorage.setItem(
            "spreadDescription",
            spreadDescription.textContent
        );

        localStorage.setItem(
            "spreadQuestion",
            question
        );

        localStorage.setItem(
            "spreadCards",
            selectedCardsCount
        );

        window.location.href = "spread.html";

    });

});


spreadButtons.forEach(button => {

    button.addEventListener("click", () => {

        selectedCardsCount = Number(button.dataset.cards);

        spreadTitle.textContent =
            button.dataset.title;

        spreadDescription.textContent =
            button.dataset.description;

        spreadModal.classList.add("active");

    });

});

spreadClose.addEventListener("click", () => {

    spreadModal.classList.remove("active");

});

spreadModal.addEventListener("click", (e) => {

    if (e.target === spreadModal) {

        spreadModal.classList.remove("active");

    }

});
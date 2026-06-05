const title =
    localStorage.getItem("spreadTitle");

const question =
    localStorage.getItem("spreadQuestion");

const cardsCount =
    Number(localStorage.getItem("spreadCards"));

document.querySelector(
    ".header h1"
).textContent = title;

document.querySelector(
    ".question-block p"
).textContent = question;

const cardsContainer =
    document.querySelector(".cards");

cardsContainer.innerHTML = "";

for (let i = 1; i <= cardsCount; i++) {

    cardsContainer.innerHTML += `
        <div class="tarot-card">
            <span>🃏</span>
            <p>Карта ${i}</p>
        </div>
    `;

}

const spreadName =
    document.getElementById("spreadName");

const spreadQuestion =
    document.getElementById("spreadQuestion");

spreadName.textContent =
    localStorage.getItem("spreadTitle") ||
    "Расклад";

spreadQuestion.textContent =
    localStorage.getItem("spreadQuestion") ||
    "Вопрос отсутствует";
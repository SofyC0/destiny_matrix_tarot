const historyCards =
    document.querySelectorAll(".history-card");

historyCards.forEach(card => {

    card.addEventListener("click", () => {

        localStorage.setItem(
            "spreadType",
            card.dataset.type
        );

        localStorage.setItem(
            "spreadTitle",
            card.dataset.title
        );

        localStorage.setItem(
            "spreadQuestion",
            card.dataset.question
        );

        window.location.href =
            "spread.html";

    });

});
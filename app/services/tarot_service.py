from app.services.draw_cards import draw_cards

from app.services.tarot_ai_service import (
    generate_tarot_reading
)


def tarot_yes_no():

    cards = draw_cards(3)

    ai_reading = generate_tarot_reading(

        spread_name="Да / Нет",

        cards=[
            card["name"]
            for card in cards
        ]
    )

    return {

        "spread": "Да / Нет",

        "cards": cards,

        "reading": ai_reading
    }


def tarot_his_thoughts():

    cards = draw_cards(3)

    ai_reading = generate_tarot_reading(

        spread_name="Его мысли обо мне",

        cards=[
            card["name"]
            for card in cards
        ]
    )

    return {

        "spread": "Его мысли обо мне",

        "cards": cards,

        "reading": ai_reading
    }


def tarot_future():

    cards = draw_cards(5)

    ai_reading = generate_tarot_reading(

        spread_name="Что меня ждет",

        cards=[
            card["name"]
            for card in cards
        ]
    )

    return {

        "spread": "Что меня ждет",

        "cards": cards,

        "reading": ai_reading
    }


def tarot_celtic_cross():

    cards = draw_cards(10)

    ai_reading = generate_tarot_reading(

        spread_name="Кельтский крест",

        cards=[
            card["name"]
            for card in cards
        ]
    )

    return {

        "spread": "Кельтский крест",

        "cards": cards,

        "reading": ai_reading
    }
import random

from app.data.tarot_cards import TAROT_CARDS


def draw_cards(count):

    cards = random.sample(
        TAROT_CARDS,
        count
    )

    result = []

    for card in cards:

        reversed_card = random.choice(
            [True, False]
        )

        result.append({

            "name": card["name"],

            "reversed": reversed_card,

            "meaning":

                card["reversed"]
                if reversed_card
                else card["upright"]
        })

    return result


def get_daily_card():

    return {
        "spread": "daily_card",
        "cards": draw_cards(1)
    }


def get_yes_no_reading():

    return {
        "spread": "yes_no",
        "cards": draw_cards(1)
    }


def get_his_thoughts_reading():

    return {
        "spread": "his_thoughts",
        "cards": draw_cards(3)
    }


def get_future_reading():

    return {
        "spread": "future",
        "cards": draw_cards(3)
    }


def get_celtic_cross():

    return {
        "spread": "celtic_cross",
        "cards": draw_cards(10)
    }
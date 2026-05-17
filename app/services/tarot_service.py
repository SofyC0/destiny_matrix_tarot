# app/services/tarot_service.py

import random

from app.data.tarot_cards import TAROT_CARDS
from app.data.tarot_spreads import TAROT_SPREADS

from app.services.tarot_ai_service import (
    generate_tarot_reading
)

from app.services.premium_service import (
    can_use_tarot,
    can_access_tarot_spread
)


# =====================================================
# RANDOM CARD
# =====================================================

def build_card(card):

    reversed_card = random.choice([True, False])

    return {

        "id": card["id"],

        "name": card["name"],

        "arcana_type": card["arcana_type"],

        "suit": card.get("suit"),

        "reversed": reversed_card,

        "meaning": (
            card["reversed"]
            if reversed_card
            else card["upright"]
        )
    }


# =====================================================
# DRAW CARDS
# =====================================================

def draw_cards(count):

    selected = random.sample(
        TAROT_CARDS,
        count
    )

    return [
        build_card(card)
        for card in selected
    ]


# =====================================================
# BUILD SPREAD
# =====================================================

def build_spread(spread_key):

    spread = TAROT_SPREADS[spread_key]

    cards = draw_cards(
        spread["cards_count"]
    )

    result_cards = []

    for index, card in enumerate(cards):

        position_name = spread["positions"][index]

        result_cards.append({

            "position": position_name,

            **card
        })

    return {

        "spread_key": spread_key,

        "spread_name": spread["name"],

        "cards": result_cards
    }


# =====================================================
# GENERATE AI READING
# =====================================================

def build_ai_reading(spread):

    return generate_tarot_reading(

        spread_name=spread["spread_name"],

        cards=[
            {
                "name": card["name"],
                "position": card["position"],
                "reversed": card["reversed"],
                "meaning": card["meaning"]
            }
            for card in spread["cards"]
        ]
    )


# =====================================================
# DAILY CARD
# =====================================================

def tarot_daily_card():

    spread = build_spread(
        "daily_card"
    )

    spread["reading"] = build_ai_reading(
        spread
    )

    return spread


# =====================================================
# YES / NO
# =====================================================

def tarot_yes_no():

    spread = build_spread(
        "yes_no"
    )

    spread["reading"] = build_ai_reading(
        spread
    )

    return spread


# =====================================================
# HIS THOUGHTS
# =====================================================

def tarot_his_thoughts():

    spread = build_spread(
        "his_thoughts"
    )

    spread["reading"] = build_ai_reading(
        spread
    )

    return spread


# =====================================================
# FUTURE
# =====================================================

def tarot_future():

    spread = build_spread(
        "future"
    )

    spread["reading"] = build_ai_reading(
        spread
    )

    return spread


# =====================================================
# CELTIC CROSS
# =====================================================

def tarot_celtic_cross():

    spread = build_spread(
        "celtic_cross"
    )

    spread["reading"] = build_ai_reading(
        spread
    )

    return spread


# =====================================================
# UNIVERSAL SPREAD
# =====================================================

def generate_spread(spread_key):

    spread = build_spread(
        spread_key
    )

    spread["reading"] = build_ai_reading(
        spread
    )

    return spread


# =====================================================
# PREMIUM + LIMIT CHECK
# =====================================================

def generate_user_spread(
        user,
        spread_key
):

    if not can_use_tarot(

            user.is_premium,

            user.tarot_spreads_used
    ):

        return {
            "error": "Tarot limit reached"
        }

    if not can_access_tarot_spread(

            user.is_premium,

            spread_key
    ):

        return {
            "error": "Premium spread"
        }

    spread = generate_spread(
        spread_key
    )

    return spread
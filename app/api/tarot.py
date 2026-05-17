from fastapi import APIRouter

from app.services.tarot_service import (
    card_of_the_day,
    yes_no_spread,
    thoughts_spread,
    future_spread,
    celtic_cross
)

from app.services.tarot_ai_service import (
    interpret_tarot_spread
)

router = APIRouter()


# =====================================
# КАРТА ДНЯ
# =====================================

@router.get("/card-of-day")
def get_card_of_day():

    spread = card_of_the_day()

    interpretation = interpret_tarot_spread(
        "Карта дня",
        spread["cards"]
    )

    return {
        "spread": spread,
        "interpretation": interpretation
    }


# =====================================
# ДА / НЕТ
# =====================================

@router.get("/yes-no")
def get_yes_no():

    spread = yes_no_spread()

    interpretation = interpret_tarot_spread(
        "Да Нет",
        spread["cards"]
    )

    return {
        "spread": spread,
        "interpretation": interpretation
    }


# =====================================
# ЕГО МЫСЛИ
# =====================================

@router.get("/thoughts")
def get_thoughts():

    spread = thoughts_spread()

    interpretation = interpret_tarot_spread(
        "Его мысли обо мне",
        spread["cards"]
    )

    return {
        "spread": spread,
        "interpretation": interpretation
    }


# =====================================
# ЧТО МЕНЯ ЖДЕТ
# =====================================

@router.get("/future")
def get_future():

    spread = future_spread()

    interpretation = interpret_tarot_spread(
        "Что меня ждет",
        spread["cards"]
    )

    return {
        "spread": spread,
        "interpretation": interpretation
    }


# =====================================
# КЕЛЬТСКИЙ КРЕСТ
# =====================================

@router.get("/celtic-cross")
def get_celtic_cross():

    spread = celtic_cross()

    interpretation = interpret_tarot_spread(
        "Кельтский крест",
        spread["cards"]
    )

    return {
        "spread": spread,
        "interpretation": interpretation
    }
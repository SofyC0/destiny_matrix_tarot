from fastapi import APIRouter
from fastapi import HTTPException

from app.services.tarot_service import (

    tarot_daily_card,

    tarot_yes_no,

    tarot_his_thoughts,

    tarot_future,

    tarot_celtic_cross
)

from app.services.tarot_ai_service import (
    generate_tarot_reading
)

from app.config.premium_config import (
    FREE_TAROT_SPREADS
)


router = APIRouter(
    prefix="/tarot",
    tags=["Tarot"]
)


# =====================================
# HELPERS
# =====================================

def build_tarot_response(
        spread_name,
        spread_data
):
    """
    Единый формат tarot response
    """

    interpretation = generate_tarot_reading(

        spread_name,

        spread_data["cards"]
    )

    return {

        "spread_name": spread_name,

        "cards": spread_data["cards"],

        "interpretation": interpretation
    }


def check_spread_access(
        spread_key,
        user=None
):
    """
    Проверка premium доступа
    """

    # free spread
    if spread_key in FREE_TAROT_SPREADS:

        return True

    # TODO:
    # заменить на реальную premium систему

    is_premium = getattr(
        user,
        "is_premium",
        False
    )

    if not is_premium:

        raise HTTPException(

            status_code=403,

            detail=(
                "Premium subscription required"
            )
        )

    return True


# =====================================
# CARD OF THE DAY
# =====================================

@router.get("/card-of-day")
def get_card_of_day():

    check_spread_access(
        "daily_card"
    )

    spread = tarot_daily_card()

    return build_tarot_response(

        "Карта дня",

        spread
    )


# =====================================
# YES / NO
# =====================================

@router.get("/yes-no")
def get_yes_no():

    check_spread_access(
        "yes_no"
    )

    spread = tarot_yes_no()

    return build_tarot_response(

        "Да / Нет",

        spread
    )


# =====================================
# THOUGHTS
# =====================================

@router.get("/thoughts")
def get_thoughts():

    check_spread_access(
        "his_thoughts"
    )

    spread = tarot_his_thoughts()

    return build_tarot_response(

        "Его мысли обо мне",

        spread
    )


# =====================================
# FUTURE
# =====================================

@router.get("/future")
def get_future():

    check_spread_access(
        "future"
    )

    spread = tarot_future()

    return build_tarot_response(

        "Что меня ждет",

        spread
    )


# =====================================
# CELTIC CROSS
# =====================================

@router.get("/celtic-cross")
def get_celtic_cross():

    check_spread_access(
        "celtic_cross"
    )

    spread = tarot_celtic_cross()

    return build_tarot_response(

        "Кельтский крест",

        spread
    )
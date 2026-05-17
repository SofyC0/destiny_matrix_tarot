from fastapi import APIRouter

from app.services.tarot_service import (
    get_daily_card,
    get_yes_no_reading,
    get_his_thoughts_reading,
    get_future_reading,
    get_celtic_cross
)

router = APIRouter(
    prefix="/tarot",
    tags=["Tarot"]
)


@router.get("/daily")
def daily_card():

    return get_daily_card()


@router.get("/yes-no")
def yes_no():

    return get_yes_no_reading()


@router.get("/his-thoughts")
def his_thoughts():

    return get_his_thoughts_reading()


@router.get("/future")
def future():

    return get_future_reading()


@router.get("/celtic-cross")
def celtic_cross():

    return get_celtic_cross()
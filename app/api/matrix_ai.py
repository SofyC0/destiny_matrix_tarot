from fastapi import APIRouter

from app.services.matrix_ai_service import (
    generate_full_matrix_analysis,
    generate_element_analysis
)

router = APIRouter(
    prefix="/matrix-ai",
    tags=["Matrix AI"]
)


@router.get("/full/{day}/{month}/{year}")
def full_analysis(
        day: int,
        month: int,
        year: int
):

    return {
        "analysis": generate_full_matrix_analysis(
            day,
            month,
            year
        )
    }


@router.get("/element/{element}/{day}/{month}/{year}")
def element_analysis(
        element: str,
        day: int,
        month: int,
        year: int
):

    return {
        "analysis": generate_element_analysis(
            element,
            day,
            month,
            year
        )
    }
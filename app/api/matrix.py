from fastapi import APIRouter

from app.services.matrix_service import (
    calculate_matrix,
    build_matrix_geometry
)

router = APIRouter(
    prefix="/matrix",
    tags=["Matrix"]
)


@router.get("/{day}/{month}/{year}")
def get_matrix(
        day: int,
        month: int,
        year: int
):

    return calculate_matrix(
        day,
        month,
        year
    )


@router.get("/geometry/{day}/{month}/{year}")
def get_geometry(
        day: int,
        month: int,
        year: int
):

    return build_matrix_geometry(
        day,
        month,
        year
    )
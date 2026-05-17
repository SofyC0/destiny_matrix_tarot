# app/api/matrix.py

from fastapi import (

    APIRouter,

    Depends,

    HTTPException,

    status
)

from app.models import (
    User
)

from app.api.auth_utils import (
    get_current_user
)

from app.services.matrix_geometry_service import (
    build_matrix_geometry
)

from app.services.matrix_interpreter import (

    interpret_center,

    interpret_business_card,

    interpret_money_channel,

    interpret_love_channel,

    interpret_destinations,

    interpret_generation_lines,

    interpret_karma_tail,

    interpret_age_arcana,

    generate_full_matrix_reading
)

from app.services.premium_service import (

    can_access_matrix_element,

    is_premium
)


router = APIRouter()


# =========================================================
# HELPERS
# =========================================================

def require_matrix_data(
        user: User
):

    if not user.matrix_data:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Matrix data not found"
        )

    return user.matrix_data


def premium_required(
        user: User,
        element_name: str
):

    if not can_access_matrix_element(

            user,
            element_name
    ):

        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="Premium required"
        )


# =========================================================
# FULL MATRIX
# =========================================================

@router.get("/me")
def get_my_matrix(

    current_user: User = Depends(
        get_current_user
    )
):

    matrix = require_matrix_data(
        current_user
    )

    return {

        "matrix": matrix,

        "is_premium": is_premium(
            current_user
        )
    }


# =========================================================
# FULL READING
# =========================================================

@router.get("/reading")
def get_full_reading(

    current_user: User = Depends(
        get_current_user
    )
):

    premium_required(

        current_user,

        "inner_square"
    )

    matrix = require_matrix_data(
        current_user
    )

    return {

        "reading": generate_full_matrix_reading(
            matrix
        )
    }


# =========================================================
# CENTER
# =========================================================

@router.get("/element/center")
def get_center(

    current_user: User = Depends(
        get_current_user
    )
):

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": interpret_center(
            matrix
        )
    }


# =========================================================
# BUSINESS CARD
# =========================================================

@router.get("/element/business-card")
def get_business_card(

    current_user: User = Depends(
        get_current_user
    )
):

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": (
            interpret_business_card(
                matrix
            )
        )
    }


# =========================================================
# MONEY CHANNEL
# =========================================================

@router.get("/element/money-channel")
def get_money_channel(

    current_user: User = Depends(
        get_current_user
    )
):

    premium_required(

        current_user,

        "money_channel"
    )

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": (
            interpret_money_channel(
                matrix
            )
        )
    }


# =========================================================
# LOVE CHANNEL
# =========================================================

@router.get("/element/love-channel")
def get_love_channel(

    current_user: User = Depends(
        get_current_user
    )
):

    premium_required(

        current_user,

        "love_channel"
    )

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": (
            interpret_love_channel(
                matrix
            )
        )
    }


# =========================================================
# DESTINATIONS
# =========================================================

@router.get("/element/destinations")
def get_destinations(

    current_user: User = Depends(
        get_current_user
    )
):

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": (
            interpret_destinations(
                matrix
            )
        )
    }


# =========================================================
# GENERATION LINES
# =========================================================

@router.get("/element/generation-lines")
def get_generation_lines(

    current_user: User = Depends(
        get_current_user
    )
):

    premium_required(

        current_user,

        "male_generation_line"
    )

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": (
            interpret_generation_lines(
                matrix
            )
        )
    }


# =========================================================
# KARMA TAIL
# =========================================================

@router.get("/element/karma-tail")
def get_karma_tail(

    current_user: User = Depends(
        get_current_user
    )
):

    premium_required(

        current_user,

        "karmic_tail"
    )

    matrix = require_matrix_data(
        current_user
    )

    return {

        "interpretation": (
            interpret_karma_tail(
                matrix
            )
        )
    }


# =========================================================
# AGE ARCANA
# =========================================================

@router.get("/age/{age}")
def get_age_arcana(

    age: int,

    current_user: User = Depends(
        get_current_user
    )
):

    if age < 0 or age > 120:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Invalid age"
        )

    matrix = require_matrix_data(
        current_user
    )

    result = interpret_age_arcana(

        matrix,
        age
    )

    if not result:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Age arcana not found"
        )

    return result


# =========================================================
# MATRIX GEOMETRY
# =========================================================

@router.get("/geometry")
def get_geometry(

    current_user: User = Depends(
        get_current_user
    )
):

    matrix = require_matrix_data(
        current_user
    )

    return build_matrix_geometry(

        current_user.birth_day,

        current_user.birth_month,

        current_user.birth_year
    )
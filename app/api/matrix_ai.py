from fastapi import APIRouter, Depends

from app.models import User

from app.api.auth_utils import get_current_user

from app.services.matrix_ai_service import (

    generate_full_matrix_reading,

    generate_element_reading,

    ask_matrix_question
)

router = APIRouter()


# ==========================================
# ПОЛНЫЙ РАЗБОР
# ==========================================

@router.get("/full-reading")
def full_reading(

    current_user: User = Depends(
        get_current_user
    )
):

    result = generate_full_matrix_reading(

        current_user.matrix_data
    )

    return {
        "reading": result
    }


# ==========================================
# РАЗБОР ЭЛЕМЕНТА
# ==========================================

@router.get("/element/{element_name}")
def element_reading(

    element_name: str,

    current_user: User = Depends(
        get_current_user
    )
):

    result = generate_element_reading(

        current_user.matrix_data,

        element_name
    )

    return {
        "reading": result
    }


# ==========================================
# AI CHAT
# ==========================================

@router.post("/ask")
def ask_question(

    question: str,

    current_user: User = Depends(
        get_current_user
    )
):

    result = ask_matrix_question(

        current_user.id,

        current_user.matrix_data,

        question
    )

    return {
        "answer": result
    }
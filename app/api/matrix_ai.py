from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.models import User

from app.api.auth_utils import get_current_user

from app.services.matrix_ai_service import (
    generate_full_matrix_reading,
    generate_element_reading,
    ask_matrix_question
)

router = APIRouter()


# ==========================================
# REQUEST MODEL
# ==========================================

class QuestionRequest(BaseModel):

    question: str


# ==========================================
# ПОЛНЫЙ РАЗБОР
# ==========================================

@router.get("/full-reading")
def full_reading(

    current_user: User = Depends(
        get_current_user
    )
):

    if not current_user.matrix_data:

        raise HTTPException(
            status_code=400,
            detail="Matrix data not found"
        )

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

    if not current_user.matrix_data:

        raise HTTPException(
            status_code=400,
            detail="Matrix data not found"
        )

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

    request: QuestionRequest,

    current_user: User = Depends(
        get_current_user
    )
):

    if not current_user.matrix_data:

        raise HTTPException(
            status_code=400,
            detail="Matrix data not found"
        )

    result = ask_matrix_question(

        current_user.id,

        current_user.matrix_data,

        request.question
    )

    return {
        "answer": result
    }
from fastapi import APIRouter, Depends

from app.models import User

from app.api.auth_utils import get_current_user

router = APIRouter()


# ==========================================
# CURRENT USER
# ==========================================

@router.get("/me")
def read_users_me(

        current_user: User = Depends(
            get_current_user
        )
):

    return {

        "id": current_user.id,

        "email": current_user.email,

        "username": current_user.username
    }


# ==========================================
# USER MATRIX
# ==========================================

@router.get("/matrix/me")
def get_my_matrix(

        current_user: User = Depends(
            get_current_user
        )
):

    return {

        "matrix": current_user.matrix_data
    }
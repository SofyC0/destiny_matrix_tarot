from fastapi import APIRouter, Depends

from app.api.auth_utils import get_current_user
from app.models import User

router = APIRouter()


@router.get("/me")
def get_my_matrix(current_user: User = Depends(get_current_user)):

    return {
        "matrix": current_user.user_data.get("matrix", {})
    }
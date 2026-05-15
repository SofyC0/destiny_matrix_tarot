from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserOut, UserDataUpdate

from app.api.auth_utils import get_current_user

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_users_me(
        current_user: User = Depends(get_current_user)
):

    return current_user


@router.get("/data")
def get_user_data(
        current_user: User = Depends(get_current_user)
):

    return {
        "user_data": current_user.user_data or {}
    }


@router.put("/data")
def update_user_data(
        update: UserDataUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    current_user.user_data = update.data

    db.commit()

    return {
        "status": "ok",
        "user_data": current_user.user_data
    }
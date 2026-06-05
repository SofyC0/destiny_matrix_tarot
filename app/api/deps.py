from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.database import get_db
from app.models import User, SessionToken
from app.api.auth_utils import decode_token


def get_current_user(
    token: str,
    db: Session = Depends(get_db)
):

    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = payload.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    # проверяем session token (ВАЖНО — у тебя есть таблица!)
    session = db.query(SessionToken).filter(
        SessionToken.token == token,
        SessionToken.is_revoked == False
    ).first()

    if not session:
        raise HTTPException(status_code=401, detail="Session expired")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
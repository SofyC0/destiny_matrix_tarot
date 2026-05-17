from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import JSON

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True
    )

    hashed_password = Column(
        String
    )

    birth_day = Column(
        Integer
    )

    birth_month = Column(
        Integer
    )

    birth_year = Column(
        Integer
    )

    matrix_data = Column(
        JSON
    )

    is_premium = Column(
        Boolean,
        default=False
    )

    tarot_spreads_used = Column(
        Integer,
        default=0
    )

    ai_questions_used = Column(
        Integer,
        default=0
    )
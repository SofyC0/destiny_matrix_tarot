from sqlalchemy import (

    Column,

    Integer,

    String,

    JSON,

    DateTime,

    Boolean,

    ForeignKey
)

from sqlalchemy.orm import (
    relationship
)

from sqlalchemy.sql import func

from app.database import Base


# ==========================================
# USER
# ==========================================

class User(Base):

    __tablename__ = "users"

    id = Column(

        Integer,

        primary_key=True,

        index=True
    )

    # auth
    email = Column(

        String(255),

        unique=True,

        index=True,

        nullable=False
    )

    username = Column(

        String(100),

        unique=True,

        index=True,

        nullable=False
    )

    hashed_password = Column(

        String(255),

        nullable=False
    )

    # premium
    is_premium = Column(

        Boolean,

        default=False,

        nullable=False
    )

    # birth date
    birth_day = Column(Integer)

    birth_month = Column(Integer)

    birth_year = Column(Integer)

    # matrix
    matrix_data = Column(JSON)

    # timestamps
    created_at = Column(

        DateTime(timezone=True),

        server_default=func.now()
    )

    updated_at = Column(

        DateTime(timezone=True),

        server_default=func.now(),

        onupdate=func.now()
    )

    # relationships
    calculations = relationship(

        "CalculationHistory",

        back_populates="user",

        cascade="all, delete-orphan"
    )

    sessions = relationship(

        "SessionToken",

        back_populates="user",

        cascade="all, delete-orphan"
    )


# ==========================================
# CALCULATION HISTORY
# ==========================================

class CalculationHistory(Base):

    __tablename__ = "calculation_history"

    id = Column(

        Integer,

        primary_key=True,

        index=True
    )

    user_id = Column(

        Integer,

        ForeignKey("users.id"),

        nullable=False,

        index=True
    )

    calculation_type = Column(

        String(50),

        nullable=False
    )

    input_data = Column(JSON)

    result_data = Column(JSON)

    created_at = Column(

        DateTime(timezone=True),

        server_default=func.now()
    )

    # relationship
    user = relationship(

        "User",

        back_populates="calculations"
    )


# ==========================================
# SESSION TOKEN
# ==========================================

class SessionToken(Base):

    __tablename__ = "session_tokens"

    id = Column(

        Integer,

        primary_key=True,

        index=True
    )

    user_id = Column(

        Integer,

        ForeignKey("users.id"),

        nullable=False,

        index=True
    )

    token = Column(

        String(500),

        unique=True,

        index=True,

        nullable=False
    )

    expires_at = Column(

        DateTime,

        nullable=False
    )

    is_revoked = Column(

        Boolean,

        default=False,

        nullable=False
    )

    created_at = Column(

        DateTime(timezone=True),

        server_default=func.now()
    )

    # relationship
    user = relationship(

        "User",

        back_populates="sessions"
    )
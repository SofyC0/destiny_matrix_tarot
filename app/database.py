import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)


# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()


# ==========================================
# DATABASE URL
# ==========================================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./users.db"
)


# ==========================================
# SQLITE CONFIG
# ==========================================

connect_args = {}

if DATABASE_URL.startswith("sqlite"):

    connect_args = {
        "check_same_thread": False
    }


# ==========================================
# ENGINE
# ==========================================

engine = create_engine(

    DATABASE_URL,

    connect_args=connect_args,

    pool_pre_ping=True
)


# ==========================================
# SESSION
# ==========================================

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine
)


# ==========================================
# BASE MODEL
# ==========================================

Base = declarative_base()


# ==========================================
# DB DEPENDENCY
# ==========================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
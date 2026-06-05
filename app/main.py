import os

from contextlib import asynccontextmanager

from dotenv import load_dotenv

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import (
    router as auth_router
)

from app.api.matrix import (
    router as matrix_router
)

from app.api.matrix_ai import (
    router as matrix_ai_router
)

from app.api.tarot import (
    router as tarot_router
)

from app.users import (
    router as users_router
)

from app.database import engine

from app.models import Base


# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()


# ==========================================
# DATABASE STARTUP
# ==========================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    Base.metadata.create_all(
        bind=engine
    )

    yield

    # shutdown
    pass


# ==========================================
# APP
# ==========================================

app = FastAPI(

    title="Destiny Matrix Tarot API",

    description=(
        "API для приложения "
        "Матрица Судьбы + Таро"
    ),

    version="1.0.0",

    lifespan=lifespan
)


# ==========================================
# CORS
# ==========================================

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "*"
).split(",")

app.add_middleware(

    CORSMiddleware,

    allow_origins=ALLOWED_ORIGINS,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ==========================================
# ROUTERS
# ==========================================

app.include_router(

    auth_router,

    prefix="/api/auth",

    tags=["Auth"]
)

app.include_router(

    users_router,

    prefix="/api/users",

    tags=["Users"]
)

app.include_router(

    matrix_router,

    prefix="/api/matrix",

    tags=["Matrix"]
)

app.include_router(

    matrix_ai_router,

    prefix="/api/matrix-ai",

    tags=["Matrix AI"]
)

app.include_router(

    tarot_router,

    prefix="/api/tarot",

    tags=["Tarot"]
)


# ==========================================
# ROOT
# ==========================================

@app.get("/")
async def root():

    return {

        "message": (
            "Destiny Matrix Tarot API "
            "работает ✨"
        ),

        "docs": "/docs",

        "version": "1.0.0"
    }


# ==========================================
# HEALTH
# ==========================================

@app.get("/health")
async def health():

    return {

        "status": "healthy"
    }
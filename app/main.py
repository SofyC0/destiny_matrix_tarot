from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.matrix import router as matrix_router
from app.users import router as users_router
from app.api.matrix_ai import router as matrix_ai_router
from app.api.tarot import router as tarot_router

from app.database import engine
from app.models import Base

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Destiny Matrix Tarot API", description="API для приложения Матрица Судьбы + Таро", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

app.include_router(matrix_ai_router, prefix="/api/matrix-ai", tags=["Matrix AI"])

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

app.include_router(users_router, prefix="/api/users", tags=["Users"])

app.include_router(matrix_router, prefix="/api/matrix", tags=["Matrix"])

app.include_router(tarot_router, prefix="/api/tarot", tags=["Tarot"])

@app.get("/")
async def root():
    return {
        "message": "Destiny Matrix Tarot API работает! ✨",
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
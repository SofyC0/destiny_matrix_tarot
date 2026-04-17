from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Импортируем роутер
from routers.auth import router as auth_router

app = FastAPI(
    title="Destiny Matrix Tarot API",
    description="API для приложения Матрица Судьбы + Таро",
    version="1.0.0"
)

# ==================== CORS ====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Для разработки оставляем *, потом изменим
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== Подключаем роутеры ====================
app.include_router(auth_router, prefix="/api", tags=["Auth"])

# ==================== Тестовые эндпоинты ====================
@app.get("/")
async def root():
    return {
        "message": "Destiny Matrix Tarot API работает! ✨",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
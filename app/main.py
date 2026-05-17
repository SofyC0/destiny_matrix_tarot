from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.matrix import router as matrix_router
from app.routers.matrix_ai import router as matrix_ai_router
from app.routers.tarot import router as tarot_router

app = FastAPI(
    title="Destiny Matrix API"
)

app.include_router(auth_router)
app.include_router(matrix_router)
app.include_router(matrix_ai_router)
app.include_router(tarot_router)


@app.get("/")
def root():
    return {
        "message": "Backend working"
    }
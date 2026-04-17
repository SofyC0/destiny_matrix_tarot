from fastapi import FastAPI
from database import engine, Base
from users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Destiny Matrix + Tarot API")

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Destiny Matrix API is running"}
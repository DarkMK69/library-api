from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine, Base

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Hello World"}
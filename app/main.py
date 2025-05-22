from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine, Base
from app.api.v1 import books, readers, borrows, auth

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(books.router, prefix="/api/v1/books", tags=["books"])
app.include_router(readers.router, prefix="/api/v1/readers", tags=["readers"])
app.include_router(borrows.router, prefix="/api/v1/borrows", tags=["borrows"])
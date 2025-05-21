from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.book import BookCreate, BookUpdate, BookInDB
from app.services.book import BookService

router = APIRouter()

@router.post("/", response_model=BookInDB)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await BookService(db).create_book(book)

@router.get("/{book_id}", response_model=BookInDB)
async def read_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await BookService(db).get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
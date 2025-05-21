from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

class BookService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_book(self, book: BookCreate):
        db_book = Book(**book.dict())
        self.db.add(db_book)
        await self.db.commit()
        await self.db.refresh(db_book)
        return db_book

    async def get_book(self, book_id: int):
        return await self.db.get(Book, book_id)
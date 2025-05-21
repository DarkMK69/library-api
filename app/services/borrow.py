from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import BorrowedBook, Book

class BorrowService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def borrow_book(self, book_id: int, reader_id: int):
        # Проверяем доступно ли книга
        book = await self.db.get(Book, book_id)
        if not book or book.quantity <= 0:
            raise ValueError("Book not available")

        # Проверяем лимит книг у читателя
        stmt = select(BorrowedBook).where(
            BorrowedBook.reader_id == reader_id,
            BorrowedBook.return_date == None
        )
        result = await self.db.execute(stmt)
        if len(result.scalars().all()) >= 3:
            raise ValueError("Reader has reached book limit")

        # Создаем запись о выдаче
        borrowed = BorrowedBook(book_id=book_id, reader_id=reader_id)
        self.db.add(borrowed)
        
        # Уменьшаем количество книг
        book.quantity -= 1
        
        await self.db.commit()
        return borrowed
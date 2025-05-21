from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.reader import Reader
from app.schemas.reader import ReaderCreate

class ReaderService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_reader(self, reader: ReaderCreate):
        db_reader = Reader(**reader.dict())
        self.db.add(db_reader)
        await self.db.commit()
        await self.db.refresh(db_reader)
        return db_reader
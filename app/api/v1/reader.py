from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.reader import ReaderCreate, ReaderInDB
from app.services.reader import ReaderService

router = APIRouter()

@router.post("/", response_model=ReaderInDB)
async def create_reader(reader: ReaderCreate, db: AsyncSession = Depends(get_db)):
    return await ReaderService(db).create_reader(reader)
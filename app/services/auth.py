from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.schemas.user import UserCreate, UserInDB
from app.core.security import get_password_hash

class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, hashed_password=hashed_password)
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user
from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: Optional[int] = None
    isbn: Optional[str] = None
    quantity: int = Field(1, ge=0)
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookInDB(BookBase):
    id: int

    class Config:
        orm_mode = True
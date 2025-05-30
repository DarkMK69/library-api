from pydantic import BaseModel, EmailStr

class ReaderBase(BaseModel):
    name: str
    email: EmailStr

class ReaderCreate(ReaderBase):
    pass

class ReaderUpdate(ReaderBase):
    pass

class ReaderInDB(ReaderBase):
    id: int

    class Config:
        orm_mode = True
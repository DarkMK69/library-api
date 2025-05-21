from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Library API"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/library"
    
    class Config:
        env_file = ".env"

settings = Settings()

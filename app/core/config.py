from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Library API"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/library"
    SECRET_KEY: str = "secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
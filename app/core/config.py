# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables (.env)
    Use this class to centralize config for the whole application
    """

    # Database
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"  # Load environment variables from .env
        env_file_encoding = "utf-8"


# Create a single settings instance to import everywhere
settings = Settings()

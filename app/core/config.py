from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "trading_signals"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"

    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"

    # External APIs
    FOREX_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
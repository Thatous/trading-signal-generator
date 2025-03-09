from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # Security
    SECRET_KEY: str
    ALGORITHM: str

    # External APIs
    FOREX_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:pass@localhost:5432/new"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

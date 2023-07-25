from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALLOWED_ORIGINS: List = ['*']
    APP_VERSION: str | None = None
    POSTGRES_HOST: str | None = None
    POSTGRES_PORT: int | None = None
    POSTGRES_DB: str | None = None
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None

    class Config:
        env_file = '.env'


settings = Settings()

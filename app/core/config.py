from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_VERSION: str | None = '0.0.0'

    class Config:
        env_file = '.env'

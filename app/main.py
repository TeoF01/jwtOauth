from functools import lru_cache

from fastapi import FastAPI, status

from core.config import Settings


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI(title='JWT Project', version=get_settings().APP_VERSION)


@app.get(path='/', status_code=status.HTTP_200_OK)
def root() -> dict:
    return {'app_version': app.version}

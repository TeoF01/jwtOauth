from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings as st

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{st.POSTGRES_USER}:{st.POSTGRES_PASSWORD}@{st.POSTGRES_HOST}:{st.POSTGRES_PORT}/{st.POSTGRES_DB}'
)

engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except exc.SQLAlchemyError as err:
        db.rollback()
        raise err
    finally:
        db.close()

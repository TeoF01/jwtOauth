from sqlalchemy import Column, String, Integer, Boolean

from db.database import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(length=100), nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, nullable=False, default=True)

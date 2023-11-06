from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from database import Base


##metadata = MetaData()


class User(SQLAlchemyBaseUserTable[int], Base): ## на f4 посмотреть внутренности штуки этой
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(75), nullable=False)
    last_name: Mapped[str] = mapped_column(String(75), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(75), nullable=False)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
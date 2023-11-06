from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import  SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean,DateTime, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DATABASE_URL = "postgresql+asyncpg://postgres:wokawoka23@localhost:5432/bd"


class Base(DeclarativeBase):
    pass


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
    ##birthdate: Mapped[DateTime]=mapped_column(DateTime,nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) ## ТИП ЭТО НАДО ИСПОЛЬЗОВАТЬ ОДИН РАЗ. ЭТО СОЗДАНИЕ БАЗЫ МОЛ ЧТОБ НЕ БЫЛО МНОГО РАЗ


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
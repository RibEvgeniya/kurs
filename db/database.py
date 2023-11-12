from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


import settings


engine = create_async_engine(settings.DATABASE_URL, echo=True)
create_session = async_sessionmaker(engine, expire_on_commit=False, future=True)

async def get_db_session() -> AsyncSession:

    try:
        session = create_session()
        yield session
    finally:
        await session.close()



from db.models import Patient
async def get_user_db(session: AsyncSession = Depends(get_db_session)):
    yield SQLAlchemyUserDatabase(session, Patient)



from db.Manager import UserManager


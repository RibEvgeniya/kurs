from typing import Annotated

from fastapi import APIRouter, Depends,HTTPException

from schemas import PatientRead, PatientCreate,PatientUpdate
from db.DALS.PacientDal import PacientDAL
from db.database import AsyncSession, get_db_session


pacient_router = APIRouter()


@pacient_router.post("/", response_model=PatientRead)
async def create_client(
    client: PatientCreate, session: Annotated[AsyncSession, Depends(get_db_session)]
):
    async with session.begin():
        client_dal = PacientDAL(session)

        old_client = await client_dal.get_client_by_email(client.email)
        if old_client:
            raise HTTPException(
                status_code=409,
                detail="client with provided email already exists"
            )

        new_client = await client_dal.create_client(
            first_name=client.first_name,
            middle_name=client.middle_name,
            last_name=client.last_name,
            phone=client.phone,
            email=client.email,
            hashed_password=client.password,
        )

        return new_client


@pacient_router.get("/{id}", response_model=PatientRead)
async def get_client(
    id: int, session: Annotated[AsyncSession, Depends(get_db_session)]
):
    async with session.begin():
        client_dal = PacientDAL(session)
        client = await client_dal.get_client_by_id(id)

        if client is None:
            raise HTTPException(
                status_code=404, detail="client with provided id does not exist"
            )

        return client


@pacient_router.put("/{id}")
async def update_client(
    id: int,
    updated_client:PatientUpdate,
    session: Annotated[AsyncSession, Depends(get_db_session)],
):
    async with session.begin():
        client_dal = PacientDAL(session)
        updated_client = await client_dal.update_client(
            id, **updated_client(exclude_unset=True)
        )
        return updated_client


@pacient_router.delete("/{id}")
async def delete_client(id: int, session: Annotated[AsyncSession, Depends(get_db_session)]):

    async with session.begin():
        clients_dal = PacientDAL(session)

        room = await clients_dal.get_client_by_id(id)
        if room is None:
            raise HTTPException(
                status_code=404, detail="client with provided id does not exist"
            )
        deleted_clients_id = await clients_dal.delete_client(id)
        return {deleted_clients_id: "is deleted"}





from fastapi_users.authentication import JWTStrategy

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
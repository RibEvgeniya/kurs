from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from db.models import Patient


class PacientDAL:
    """Data Access Layer for operating clients info"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_client(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        phone: str,
        email: str,
        hashed_password: str,
        is_active: bool = True,
    ) -> Patient:
        new_client = Patient(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            phone=phone,
            email=email,
            hashed_password=hashed_password,
            is_active=is_active,
        )
        self.session.add(new_client)
        await self.session.flush()
        return new_client

    async def delete_client(self, client_id: int) -> int | None:
        query = (
            update(Patient)
            .where(Patient.id == client_id & Patient.is_active == True)
            .values(is_active=False)
            .returning(Patient.id)
        )
        res = await self.session.execute(query)
        deleted_user_id = res.scalar_one_or_none()
        return deleted_user_id

    async def get_client_by_id(
        self, client_id: int, include_his_room_orders: bool = False
    ) -> Patient | None:
        query = select(Patient).where(Patient.id == client_id)

        if include_his_room_orders:
            query.options(joinedload(Patient.room_orders))

        res = await self.session.execute(query)
        client = res.scalar_one_or_none()
        return client

    async def get_client_by_email(self, client_email: str) -> Patient | None:
        query = select(Patient).where(Patient.email == client_email)
        res = await self.session.execute(query)
        client = res.scalar_one_or_none()
        return client

    async def get_clients(
        self, offset: int, limit: int, active_ones: bool = None
    ) -> list[Patient]:
        query = (
            select(Patient)
            .options(joinedload(Patient.room_orders))
            .offset(offset)
            .limit(limit)
        )

        if active_ones is not None:
            query.where(Patient.is_active == active_ones)

        res = await self.session.execute(query)
        clients = res.scalars().unique()

        return list(clients)

    async def update_client(self, client_id: int, **kwargs):
        query = (
            update(Patient)
            .where(Patient.id == client_id)
            .values(kwargs)
            .returning(Patient)
        )
        res = await self.session.execute(query)
        updated_client = res.scalar_one_or_none()
        return updated_client


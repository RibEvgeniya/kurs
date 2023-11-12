from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

#from db.models import Post, PermissionsEnum
from db.models import Specialisation, PermissionsEnum

class PostDAL:
    """Data Access Layer for operating posts info"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_post(
        self, post_name: str, permissions: list[PermissionsEnum]
    ) -> Specialisation:
        new_post = Specialisation(name=post_name, permissions=[p.value for p in permissions])
        self.session.add(new_post)
        await self.session.flush()
        return new_post

    async def delete_post(
        self, post_id: int = None, post_name: int = None
    ) -> int | None:
        query = delete(Specialisation).where(Specialisation.id == post_id).returning(Specialisation.id)
        res = await self.session.execute(query)
        deleted_post_id = res.scalar_one_or_none()
        return deleted_post_id

    async def get_post_by_id(self, post_id: int) -> Specialisation| None:
        query = select(Specialisation).where(Specialisation.id == post_id)

        res = await self.session.execute(query)
        post = res.scalar_one_or_none()
        return post

    async def get_post_by_name(self, post_name: str) -> Specialisation | None:
        query = select(Specialisation).where(Specialisation.name == post_name)
        res = await self.session.execute(query)
        post = res.scalar_one_or_none()
        return post

    async def get_posts(self, offset: int, limit: int) -> list[Specialisation]:
        query = select(Post).offset(offset).limit(limit)

        res = await self.session.execute(query)
        posts = res.scalars().unique()

        return list(posts)

    async def update_post(self, post_id: int, **kwargs):
        query = update(Specialisation).where(Specialisation.id == post_id).values(kwargs).returning(Specialisation.id)
        res = await self.session.execute(query)
        updated_post_id = res.scalar_one_or_none()
        return updated_post_id

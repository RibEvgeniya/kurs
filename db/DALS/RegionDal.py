from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

#from db.models import Post, PermissionsEnum
from db.models import Region

class RegionDAL:
    """Data Access Layer for operating posts info"""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_region(
        self, area: str,
    ) -> Region:
        new_region = Region(area=area)
        self.session.add(new_region)
        await self.session.flush()
        return new_region
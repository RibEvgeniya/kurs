from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import RegionShow, RegionCreate, RegionUpdate
from db.DALS.RegionDal import RegionDAL
from db.database import AsyncSession, get_db_session



region_router = APIRouter()
@region_router.post("/")
async def create_post(
    region: RegionCreate, session: Annotated[AsyncSession, Depends(get_db_session)]
):
    async with session.begin():
        post_dal = RegionDAL(session)
        new_post = await post_dal.create_region(
            area=region.area,
        )
        return new_post

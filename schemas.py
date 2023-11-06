import datetime
from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel, EmailStr



class PatientRead(schemas.BaseUser[int]): ## стоит смотреть в исходники на ф4 чтоб посмотреть чо внутри
    id: int
    first_name: str
    middle_name: str
    last_name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = True
    birthdate: datetime.date
    phone: str
    polis:str
    class Config:
        orm_mode = True


class PatientCreate(schemas.BaseUserCreate):
    first_name: str
    middle_name:str
    last_name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = True
    birthdate: datetime.date
    phone: str
    polis:str

class PatientUpdate(schemas.BaseUserUpdate):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = True
    birthdate: Optional[datetime.date]
    phone: Optional[str ]=None
    polis: Optional[str]=None
import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth import auth_backend
from database import User
from manager import get_user_manager
from schema import UserRead, UserCreate




app1 = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app1.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)



app1.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
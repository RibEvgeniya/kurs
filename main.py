from fastapi import FastAPI, status, HTTPException, Depends
import asyncio

from fastapi_users import FastAPIUsers
from routers.pacient import pacient_router
from db.models import Patient
from db.Manager import get_user_manager
from auth import auth_backend
from schemas import PatientCreate, PatientRead, PatientUpdate


app=FastAPI()



app.include_router(pacient_router, prefix="/patients", tags=["patients"])




fastapi_users = FastAPIUsers[Patient, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)



app.include_router(
    fastapi_users.get_register_router(PatientRead, PatientCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(PatientRead),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(PatientRead, PatientUpdate, requires_verification=True),
    prefix="/users",
    tags=["users"],
)


current_user = fastapi_users.current_user()
from db.models import Patient
@app.get("/protected-route")
def protected_route(user: Patient = Depends(current_user)):
    return f"Hello, {user.email}"


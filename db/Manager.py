import uuid
from typing import Optional, Union, Dict, Any

from fastapi import Depends, Request, exceptions
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException, schemas, models

from db.models import Patient
from db.database import get_user_db
from schemas import PatientCreate

SECRET = "SECRET"





class UserManager(IntegerIDMixin, BaseUserManager[Patient, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: Patient, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: Patient, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify( ## Typically, you'll want to send an e-mail with the link (and the token) that allows the user to verify their e-mail.
        self, user: Patient, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


    async def validate_password(
            self,
            password: str,
            user: Union[PatientCreate, Patient],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

    async def on_after_update(
            self,
            user: Patient,
            update_dict: Dict[str, Any],
            request: Optional[Request] = None,
    ):
        print(f"User {user.id} has been updated with {update_dict}.")

    async def create(
            self,
            user_create: schemas.UC,
            safe: bool = False,
            request: Optional[Request] = None,
    ) -> schemas.U: ## здесь было через модел что-то
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        ##user_dict["is_verified"]=True
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        ##user_dict[""] =
        ##user_dict["role_id"] = 1

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
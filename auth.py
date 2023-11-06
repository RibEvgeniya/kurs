from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import JWTStrategy


PRIVATE_KEY = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=PRIVATE_KEY,
        lifetime_seconds=3600,
       ## algorithm="RS256",
        ##public_key=PUBLIC_KEY,
    )


cookie_transport = CookieTransport(cookie_name="some",cookie_max_age=3600,cookie_domain=None)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
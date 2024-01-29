from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_max_age=1500)

SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=1500)

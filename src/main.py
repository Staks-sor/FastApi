import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from operations.router import router as router_operation
from redis import asyncio as aioredis

if __name__ == "__main__":
    app = FastAPI(
        title="Trading App"
    )

    app.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth",
        tags=["Auth"],
    )

    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["Auth"],
    )


    @app.on_event("startup")
    async def startup():
        redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    app.include_router(router_operation)
    uvicorn.run(app)
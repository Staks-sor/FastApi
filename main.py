import uvicorn
from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import ValidationError

from app import my_app
from another_class import another_class
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

if __name__ == "__main__":
    app = FastAPI(
        title="Мое приложение"
    )

    fastapi_users = FastAPIUsers[User, int](
        get_user_manager,
        [auth_backend],
    )

    app.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth/jwt",
        tags=["auth"],
    )

    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )


    @app.exception_handler(ValidationException)
    async def validation_exception_handler(exc: ValidationException):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": exc.errors()})
        )


    app.include_router(my_app.app)
    app.include_router(another_class.app)

    uvicorn.run(app)

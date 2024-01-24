import uvicorn
from fastapi import FastAPI
from pydantic import ValidationError

from app import my_app
from another_class import another_class
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

if __name__ == "__main__":
    app = FastAPI(
        title="Мое приложение"
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

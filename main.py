import uvicorn
from fastapi import FastAPI
from app import my_app
from another_class import another_class

if __name__ == "__main__":
    app = FastAPI(
        title="Мое приложение"
    )

    app.include_router(my_app.app)
    app.include_router(another_class.app)

    uvicorn.run(app)

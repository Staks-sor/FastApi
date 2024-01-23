from fastapi import APIRouter

from app import my_app


class AnotherClass:
    def __init__(self, my_app):
        self.app = APIRouter()
        self.my_app = my_app
        self.some_method()

    def some_method(self):
        @self.app.get("/us/")
        async def users() -> int:
            number = 880000000000
            return number

    def setup_routes(self):
        self.my_app.include_router(self.app)


another_class = AnotherClass(my_app)

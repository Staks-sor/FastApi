from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field

fake_user = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"}
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12}
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float = Field(ge=0)
    amount: float

class Degree(BaseModel):
    id: int

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: List[Degree]

class MyApp:
    def __init__(self):
        self.app = APIRouter()
        self.setup_routes()
        self.user_agent()

    def setup_routes(self):
        @self.app.get("/")
        async def hello() -> str:
            number = 45
            s = f"Hello world! {number} и вот так вот"
            return s

    def user_agent(self):
        @self.app.get("/users/{user_id}", response_model=List[User])
        async def users(user_id: int):
            return [user for user in fake_user if user.get("id") == user_id]

        @self.app.post("/users/{user_id}")
        async def change_user_name(user_id: int, new_name: str):
            current_user = list(filter(lambda user: user.get("id") == user_id, fake_user))[0]
            current_user["name"] = new_name
            return {"status": 200, "data": current_user}

        @self.app.get("/trades")
        async def get_trades(limit: int = 1, offset: int = 0):
            return fake_trades[offset:][:limit]

        @self.app.post("/trades")
        async def add_trades(trades: List[Trade]):
            fake_trades.extend(trades)
            return {"status": 200, "data": fake_trades}


my_app = MyApp()

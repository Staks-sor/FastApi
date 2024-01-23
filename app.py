from fastapi import APIRouter

fake_user = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"}
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12}
]


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
        @self.app.get("/users/{user_id}")
        async def users(user_id: int):
            return [user for user in fake_user if user.get("id") == user_id]


my_app = MyApp()

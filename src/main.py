from fastapi import FastAPI

from src.database import create_tables
from src.routers import account_router, bank_router
from src.models.transaction import Transaction

app = FastAPI()
app.include_router(account_router)
app.include_router(bank_router)


create_tables()


@app.get("/")
def main():
    return {"Hello": "World"}

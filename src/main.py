from fastapi import FastAPI

from src.database import create_tables
from src.routers import api_router

app = FastAPI()
app.include_router(api_router)


create_tables()


@app.get("/")
def main():
    return {"Hello": "World"}

from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from src.database import create_tables
from src.routers import api_router
from src.dependencies import get_current_user

app = FastAPI()
app.include_router(api_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

create_tables()


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/me")
def read_current_user(current_user: str = Depends(get_current_user)):
    return {"email": current_user}

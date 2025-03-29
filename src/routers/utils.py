from typing import Type, TypeVar

from fastapi import APIRouter, Depends
from sqlmodel import Session, select, SQLModel
from pydantic import BaseModel

from src.database import get_session

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


def create_router(
    model: Type[ModelType], model_create: Type[CreateSchemaType], prefix: str, tag: str
) -> APIRouter:
    router = APIRouter(prefix=prefix, tags=[tag])

    @router.get("/", response_model=list[model])
    def get_items(session: Session = Depends(get_session)):
        return session.exec(select(model)).all()

    @router.post("/", response_model=model)
    def create_item(item: model_create, session: Session = Depends(get_session)):
        new_item = model.model_validate(item)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item

    return router

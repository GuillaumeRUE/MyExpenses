from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.models.account import Account


class BankBase(SQLModel):
    name: str


class Bank(BankBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    accounts: list["Account"] = Relationship(back_populates="bank")


class BankCreate(BankBase):
    pass

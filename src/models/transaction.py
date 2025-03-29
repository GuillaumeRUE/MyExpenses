from typing import TYPE_CHECKING, Optional
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Enum as SAEnum

from src.core.enums import Currency

if TYPE_CHECKING:
    from src.models.account import Account


class TransactionBase(SQLModel):
    amount: float
    date: datetime = Field(index=True)
    description: str | None = Field(default=None)
    currency: Currency = Field(sa_column=Column(SAEnum(Currency)))
    account_id: int = Field(foreign_key="account.id")


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    account: Optional["Account"] = Relationship(back_populates="transactions")


class TransactionCreate(SQLModel):
    pass

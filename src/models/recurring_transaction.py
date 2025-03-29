from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import Enum as SAEnum


from src.core.enums import Currency, Recurrency

if TYPE_CHECKING:
    from src.models.account import Account


class RecurringTransactionBase(SQLModel):
    amount: float
    description: str
    currency: Currency = Field(sa_column=Column(SAEnum(Currency)))
    recurrency_type: Recurrency = Field(sa_column=Column(SAEnum(Recurrency)))
    recurrence_interval: int  # e.g., 1 for monthly, 2 for bi-weekly
    start_date: datetime
    end_date: datetime | None = Field(default=None)
    account_id: int = Field(foreign_key="account.id")


class RecurringTransaction(RecurringTransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    account: Optional["Account"] = Relationship(back_populates="recurring_transactions")


class RecurringTransactionCreate(RecurringTransactionBase):
    pass

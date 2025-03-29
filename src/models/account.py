from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Enum as SAEnum

from src.core.enums import AccountType

if TYPE_CHECKING:
    from src.models.bank import Bank
    from src.models.transaction import Transaction
    from src.models.recurring_transaction import RecurringTransaction


class AccountBase(SQLModel):
    name: str = Field(index=True)
    bank_id: int = Field(foreign_key="bank.id")
    type: AccountType = Field(sa_column=Column(SAEnum(AccountType)))


class Account(AccountBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    bank: Optional["Bank"] = Relationship(back_populates="accounts")
    transactions: list["Transaction"] = Relationship(back_populates="account")
    recurring_transactions: list["RecurringTransaction"] = Relationship(
        back_populates="account"
    )


class AccountCreate(AccountBase):
    pass

from fastapi import APIRouter

from src.models.account import Account, AccountCreate
from src.models.bank import Bank, BankCreate
from src.models.transaction import Transaction, TransactionCreate
from src.models.recurring_transaction import (
    RecurringTransaction,
    RecurringTransactionCreate,
)

from src.routers.utils import create_router

models = [
    (Account, AccountCreate, "/accounts", "Account"),
    (Bank, BankCreate, "/banks", "Bank"),
    (Transaction, TransactionCreate, "/transactions", "Transaction"),
    (
        RecurringTransaction,
        RecurringTransactionCreate,
        "/recurring_transactions",
        "Recurring Transaction",
    ),
]

api_router = APIRouter()

for model, model_create, prefix, tag in models:
    api_router.include_router(create_router(model, model_create, prefix, tag))

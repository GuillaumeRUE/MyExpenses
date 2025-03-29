from src.models.recurring_transaction import (
    RecurringTransaction,
    RecurringTransactionCreate,
)
from src.routers.utils import create_router

recurring_transaction_router = create_router(
    RecurringTransaction,
    RecurringTransactionCreate,
    "/recurring_transactions",
    "Recurring Transaction",
)

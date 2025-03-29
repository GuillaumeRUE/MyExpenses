from src.models.transaction import Transaction, TransactionCreate
from src.routers.utils import create_router

transaction_router = create_router(
    Transaction, TransactionCreate, "/transactions", "Transaction"
)

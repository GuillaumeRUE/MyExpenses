from fastapi import APIRouter

from src.routers.auth import auth_router
from src.routers.account import account_router
from src.routers.bank import bank_router
from src.routers.transaction import transaction_router
from src.routers.recurring_transaction import recurring_transaction_router


api_router = APIRouter()

api_router.include_router(account_router)
api_router.include_router(bank_router)
api_router.include_router(transaction_router)
api_router.include_router(recurring_transaction_router)
api_router.include_router(auth_router)

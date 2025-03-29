from src.models.bank import Bank, BankCreate
from src.routers.utils import create_router


bank_router = create_router(Bank, BankCreate, "/banks", "Bank")

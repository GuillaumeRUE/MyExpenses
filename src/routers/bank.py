from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.database import get_session
from src.models.bank import Bank, BankCreate

bank_router = APIRouter(prefix="/banks", tags=["Bank"])


@bank_router.get("/", response_model=list[Bank])
def get_banks(session: Session = Depends(get_session)):
    banks = session.exec(select(Bank)).all()
    return banks


@bank_router.post("/", response_model=Bank)
def create_account(bank: BankCreate, db: Session = Depends(get_session)):
    new_bank = Bank.model_validate(bank)
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank

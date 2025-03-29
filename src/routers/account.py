from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.database import get_session
from src.models.account import Account, AccountCreate

account_router = APIRouter(prefix="/accounts", tags=["Account"])


@account_router.get("/", response_model=list[Account])
def get_accounts(session: Session = Depends(get_session)):
    accounts = session.exec(select(Account)).all()
    return accounts


@account_router.post("/", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_session)):
    new_account = Account.model_validate(account)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account
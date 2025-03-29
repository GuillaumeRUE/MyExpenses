from datetime import datetime

from fastapi import Depends, Query
from sqlmodel import Session, select

from src.database import get_session
from src.models.account import Account, AccountCreate
from src.routers.utils import create_router
from src.core.services.account_service import AccountService

account_router = create_router(Account, AccountCreate, "/accounts", "Account")


@account_router.get("/{account_id}/current_balance")
def get_current_balance(
    account_id: int, session: Session = Depends(get_session)
) -> float:
    account = session.exec(select(Account).filter(Account.id == account_id)).first()
    if not account:
        raise ValueError(f"Account with ID {account_id} not found.")

    account_service = AccountService(account)
    return account_service.get_account_balance()


@account_router.get("/{account_id}/future_balance")
def get_future_balance(
    account_id: int,
    target_date: str = Query(..., description="Target date in YYYY-MM-DD format"),
    session: Session = Depends(get_session),
) -> float:
    account = session.exec(select(Account).filter(Account.id == account_id)).first()
    if not account:
        raise ValueError(f"Account with ID {account_id} not found.")

    try:
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD"}

    account_service = AccountService(account)
    return account_service.get_future_balance(target_date_obj)

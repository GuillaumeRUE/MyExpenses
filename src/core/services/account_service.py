from typing import Optional
from datetime import datetime

from src.models.account import Account
from src.models.transaction import Transaction
from src.core.recurrence import get_next_occurrence


class AccountService:

    def __init__(self, account: Account) -> None:
        self.account = account

    def get_account_balance(
        self, extra_transactions: Optional[list[Transaction]] = None
    ) -> float:
        amount_to_add: float = 0

        if extra_transactions:
            amount_to_add = sum(
                transaction.amount for transaction in extra_transactions
            )

        return (
            sum(transaction.amount for transaction in self.account.transactions)
            + amount_to_add
        )

    def get_future_balance(self, target_date: datetime) -> float:
        list_future_transactions = self.get_future_recurring_transactions(target_date)

        return self.get_account_balance(extra_transactions=list_future_transactions)

    def get_future_recurring_transactions(
        self, target_date: datetime
    ) -> list[Transaction]:

        list_future_transaction: list[Transaction] = []

        for recurring_transaction in self.account.recurring_transactions:

            # Check if the recurrence is still active by comparing the target_date with start and end dates
            if (
                recurring_transaction.end_date
                and target_date > recurring_transaction.end_date
            ):
                continue  # Skip recurring transactions that should no longer occur

            current_date = recurring_transaction.start_date

            while current_date <= target_date:
                # Generate the future transactions on their scheduled date
                future_transaction_dict = {
                    "account_id": self.account.id,
                    "amount": recurring_transaction.amount,
                    "description": recurring_transaction.description,
                    "date": current_date,
                }
                future_transaction = Transaction(**future_transaction_dict)
                list_future_transaction.append(future_transaction)

                # Move to the next occurrence based on recurrence type
                current_date = get_next_occurrence(
                    current_date, recurring_transaction.recurrency_type
                )

        return list_future_transaction

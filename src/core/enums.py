from enum import Enum


class Currency(str, Enum):
    EUR = "EUR"
    USD = "USD"


class AccountType(str, Enum):
    CHECKING = "Checking account"
    SAVING = "Savings account"
    INVESTMENT = "Investment account"
    PEA = "PEA"


class Recurrency(str, Enum):
    YEARLY = "yearly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

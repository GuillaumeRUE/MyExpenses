from datetime import datetime
from dateutil.relativedelta import relativedelta

from src.core.enums import Recurrency


def get_next_occurrence(current_date: datetime, recurrence_type: str) -> datetime:
    recurrence_mapping = {
        Recurrency.MONTHLY: relativedelta(months=1),
        Recurrency.WEEKLY: relativedelta(weeks=1),
        Recurrency.YEARLY: relativedelta(years=1),
    }

    if recurrence_type not in recurrence_mapping:
        raise ValueError(f"Unsupported recurrence type: {recurrence_type}")

    return current_date + recurrence_mapping[recurrence_type]

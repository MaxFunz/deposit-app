from datetime import datetime, timedelta
from fastapi import HTTPException

def parse_date(date_str: str) -> datetime.date:
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Дата должна быть в формате dd.mm.yyyy")

def get_last_day_of_month(date: datetime.date) -> datetime.date:
    next_month = date.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)


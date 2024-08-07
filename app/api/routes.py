from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from ..schemas import DepositParams, CalculationResult
from ..db.models import Deposit
from ..db.database import get_db
from ..core.utils import parse_date

router = APIRouter()

def get_last_day_of_month(current_date):
    next_month = current_date.month % 12 + 1
    next_month_year = current_date.year + (current_date.month // 12)
    first_of_next_month = current_date.replace(day=1, month=next_month, year=next_month_year)
    last_day_of_current_month = first_of_next_month - timedelta(days=1)
    return last_day_of_current_month

@router.get('/calculation', response_model=List[CalculationResult])
def get_calculation(params: DepositParams = Depends(), db: Session = Depends(get_db)):
    start_date = parse_date(params.date)

    result = []
    current_date = start_date

    for _ in range(params.periods):
        params.amount *= (1 + (params.rate / 100) / 12)

        params.amount = round(params.amount, 2)

        last_day_of_current_month = get_last_day_of_month(current_date)

        formatted_date = last_day_of_current_month.strftime("%d.%m.%Y")

        result.append({
            "date": formatted_date,
            "amount": round(params.amount, 2)
        })

        deposit = Deposit(date=last_day_of_current_month, amount=params.amount)
        db.add(deposit)
        db.commit()

        current_date = last_day_of_current_month + timedelta(days=1)
    return result


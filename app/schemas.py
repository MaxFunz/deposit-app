from pydantic import BaseModel
from typing import List

class CalculationResult(BaseModel):
    date: str
    amount: float

class DepositParams(BaseModel):
    date: str
    periods: int
    amount: float
    rate: float
from datetime import datetime
from fastapi import HTTPException
from deposit_app.core.utils import parse_date, get_last_day_of_month
import pytest

def test_parse_date():
    date_str = "01.01.2023"
    date = parse_date(date_str)
    assert date == datetime.strptime(date_str, "%d.%m.%Y").date()

def test_parse_date_invalid():
    with pytest.raises(HTTPException) as excinfo:
        parse_date("invalid-date")
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Дата должна быть в формате dd.mm.yyyy"

def test_get_last_day_of_month():
    date = datetime.strptime("15.01.2023", "%d.%m.%Y").date()
    last_day = get_last_day_of_month(date)
    assert last_day == datetime.strptime("31.01.2023", "%d.%m.%Y").date()
import pytest
from sqlalchemy.orm import Session
from datetime import datetime
from deposit_app.db.models import Deposit
from deposit_app.db.database import get_test_db, TestingEngine, Base

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=TestingEngine)
    Base.metadata.create_all(bind=TestingEngine)
    yield
    Base.metadata.drop_all(bind=TestingEngine)

def test_create_deposit():
    db: Session = next(get_test_db())
    deposit = Deposit(date=datetime.strptime("31.01.2023", "%d.%m.%Y").date(), amount=1000.0)
    db.add(deposit)
    db.commit()
    db.refresh(deposit)
    assert deposit.id is not None
    assert deposit.date == datetime.strptime("31.01.2023", "%d.%m.%Y").date()
    assert deposit.amount == 1000.0


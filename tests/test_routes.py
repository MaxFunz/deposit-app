import pytest
from fastapi.testclient import TestClient
from deposit_app.main import app
from deposit_app.db.database import Base, get_test_db, TestingEngine, get_db

client = TestClient(app)

app.dependency_overrides[get_db] = get_test_db

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=TestingEngine)
    Base.metadata.create_all(bind=TestingEngine)
    yield
    Base.metadata.drop_all(bind=TestingEngine)

def test_get_calculation():
    response = client.get("/calculation", params={
        "date": "01.01.2023",
        "periods": 12,
        "amount": 1000,
        "rate": 5.0
    })
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 12
    assert data[0]["date"] == "31.01.2023"
    assert data[0]["amount"] > 1000

def test_get_calculation_invalid_date():
    response = client.get("/calculation", params={
        "date": "invalid-date",
        "periods": 12,
        "amount": 1000,
        "rate": 5.0
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Дата должна быть в формате dd.mm.yyyy"}

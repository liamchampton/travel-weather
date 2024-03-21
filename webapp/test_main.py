from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_monthly_average_valid():
    response = client.get("/countries/england/london/june")
    assert response.status_code == 200
    assert response.json() == {"high" : 64, "low" : 52}

def test_monthly_average_invalid():
    response = client.get("/countries/invalid/invalid/invalid")
    assert response.status_code == 404
    assert response.json() == {"detail" : "invalid country, city or month"}
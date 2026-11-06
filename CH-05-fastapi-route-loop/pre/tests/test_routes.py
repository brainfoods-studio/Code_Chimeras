import pytest
from fastapi.testclient import TestClient

from reportsapi.main import app

client = TestClient(app)


def test_sales_route_returns_the_report():
    response = client.get("/reports/sales")
    assert response.status_code == 200
    assert response.json()["total_cents"] == 223000


def test_refunds_route_returns_the_report():
    response = client.get("/reports/refunds")
    assert response.status_code == 200

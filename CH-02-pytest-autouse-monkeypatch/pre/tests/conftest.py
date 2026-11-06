import pytest

from payments.client import ChargeResult


@pytest.fixture(autouse=True)
def _no_real_charges(monkeypatch):
    monkeypatch.setattr(
        "payments.client.charge",
        lambda customer_id, amount_cents, currency="usd": ChargeResult(
            ok=True, charge_id="ch_test"
        ),
    )

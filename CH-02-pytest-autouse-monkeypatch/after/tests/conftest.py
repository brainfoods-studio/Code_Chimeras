import pytest

from payments import checkout
from tests.fakes import FakeCharge


@pytest.fixture
def fake_charge(monkeypatch: pytest.MonkeyPatch) -> FakeCharge:
    fake = FakeCharge()
    # checkout.py does "from payments.gateway import charge", so the name
    # that checkout() looks up lives in payments.checkout.
    monkeypatch.setattr(checkout, "charge", fake)
    return fake

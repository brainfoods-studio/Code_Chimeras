import pytest

from payments.checkout import EmptyCartError, PaymentDeclined, Receipt, checkout
from payments.gateway import ChargeResult
from tests.fakes import FakeCharge


def test_checkout_charges_the_cart_total(fake_charge: FakeCharge):
    receipt = checkout("cus_42", [1200, 800])
    assert fake_charge.calls == [("cus_42", 2000, "usd")]
    assert receipt == Receipt(charge_id="ch_test", amount_cents=2000)


def test_checkout_rejects_an_empty_cart(fake_charge: FakeCharge):
    with pytest.raises(EmptyCartError):
        checkout("cus_42", [])
    assert fake_charge.calls == []


def test_checkout_raises_when_the_card_is_declined(fake_charge: FakeCharge):
    fake_charge.result = ChargeResult(ok=False, charge_id="", decline_code="card_declined")
    with pytest.raises(PaymentDeclined, match="card_declined"):
        checkout("cus_42", [500])

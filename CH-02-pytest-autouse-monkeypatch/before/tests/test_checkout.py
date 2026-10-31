import pytest

from payments.checkout import EmptyCartError, Receipt, checkout


def test_checkout_returns_receipt_for_the_cart_total():
    receipt = checkout("cus_42", [1200, 800])
    assert receipt == Receipt(charge_id="ch_test", amount_cents=2000)


def test_checkout_rejects_an_empty_cart():
    with pytest.raises(EmptyCartError):
        checkout("cus_42", [])


def test_checkout_uses_the_receipt_charge_id():
    assert checkout("cus_42", [500]).charge_id == "ch_test"

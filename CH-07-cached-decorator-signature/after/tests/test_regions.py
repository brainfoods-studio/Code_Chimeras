import inspect

from pricing_service.checkout import cart_total_cents
from pricing_service.invoices import invoice_line_cents
from pricing_service.pricing import quote_price


def test_invoice_line_uses_its_own_region():
    assert cart_total_cents([("kb-100", 2)], region="US") == 9800
    assert invoice_line_cents("kb-100", 2, "EUR", "IN") == 11564


def test_default_and_explicit_arguments_share_one_entry():
    first = quote_price("hub-300", 3)
    assert quote_price("hub-300", 3, "EUR", region="EU") == first


def test_decorated_function_keeps_its_signature():
    assert quote_price.__name__ == "quote_price"
    assert list(inspect.signature(quote_price).parameters) == ["sku", "qty", "currency", "region"]

from pricing_service.checkout import cart_total_cents
from pricing_service.pricing import quote_price


def test_quote_price_uses_base_price():
    assert quote_price("ms-200", 4) == 10000


def test_quote_price_converts_currency():
    assert quote_price("hub-300", 10, "USD") == 85320


def test_cart_total_adds_each_line():
    assert cart_total_cents([("ms-200", 2), ("ms-200", 1)]) == 7500

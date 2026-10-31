from pricing_service.checkout import cart_total_cents
from pricing_service.pricing import quote_price


def test_quote_price_applies_region_tax():
    assert quote_price("ms-200", 4, region="US") == 10000


def test_quote_price_converts_currency():
    assert quote_price("hub-300", 10, "USD", region="EU") == 102384


def test_cart_total_adds_each_line():
    assert cart_total_cents([("ms-200", 2), ("ms-200", 1)], region="US") == 7500

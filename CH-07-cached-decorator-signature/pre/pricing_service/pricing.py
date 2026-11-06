from pricing_service.cache import cached

PRICES_CENTS = {"kb-100": 4900, "ms-200": 2500, "hub-300": 7900}
CURRENCY_MILLI = {"EUR": 1000, "USD": 1080}


@cached(ttl=60)
def quote_price(sku, qty, currency="EUR"):
    base = PRICES_CENTS[sku] * qty
    return base * CURRENCY_MILLI[currency] // 1000

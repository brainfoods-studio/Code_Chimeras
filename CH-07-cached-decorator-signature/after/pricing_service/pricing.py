from pricing_service.cache import cached

PRICES_CENTS = {"kb-100": 4900, "ms-200": 2500, "hub-300": 7900}
CURRENCY_MILLI = {"EUR": 1000, "USD": 1080}
TAX_BASIS_POINTS = {"EU": 2000, "US": 0, "IN": 1800}


@cached(ttl=60)
def quote_price(sku, qty, currency="EUR", *, region="EU"):
    base = PRICES_CENTS[sku] * qty
    converted = base * CURRENCY_MILLI[currency] // 1000
    return converted * (10000 + TAX_BASIS_POINTS[region]) // 10000

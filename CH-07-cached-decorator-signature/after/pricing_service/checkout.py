from pricing_service.pricing import quote_price


def cart_total_cents(items, region):
    return sum(quote_price(sku, qty, region=region) for sku, qty in items)

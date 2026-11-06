from pricing_service.pricing import quote_price


def cart_total_cents(items):
    return sum(quote_price(sku, qty) for sku, qty in items)

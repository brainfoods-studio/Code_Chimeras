from pricing_service.pricing import quote_price


def invoice_line_cents(sku, qty, currency):
    return quote_price(sku, qty, currency=currency)

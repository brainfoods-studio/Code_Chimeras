import pytest

from pricing_service.checkout import cart_total_cents
from pricing_service.invoices import invoice_line_cents


# Written as it would be written; it fails as expected (xfail). After the region edit,
# quote_price takes a keyword-only region, but the cache wrapper in cache.py builds its
# key from positional arguments only. The checkout quote for US caches ("kb-100", 2),
# and the invoice line for IN then reads that same entry and returns the US price.
@pytest.mark.xfail(strict=True, reason="cache key ignores keyword arguments, so region IN returns the cached region US price")
def test_invoice_line_uses_its_own_region():
    assert cart_total_cents([("kb-100", 2)], region="US") == 9800
    assert invoice_line_cents("kb-100", 2, "EUR", "IN") == 11564

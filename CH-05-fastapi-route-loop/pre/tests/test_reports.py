from reportsapi.reports import build_inventory_report, build_refunds_report, build_sales_report


def test_sales_report_totals_all_regions():
    assert build_sales_report(2026) == {"report": "sales", "year": 2026, "total_cents": 223000}


def test_refunds_report_totals_all_refunds():
    report = build_refunds_report(2026)
    assert report["total_cents"] == 6500


def test_inventory_report_counts_units_in_one_warehouse():
    assert build_inventory_report("main")["units"] == 52

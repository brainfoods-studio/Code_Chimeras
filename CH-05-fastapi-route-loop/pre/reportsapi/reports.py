SALES = [
    {"region": "north", "amount_cents": 125000},
    {"region": "south", "amount_cents": 98000},
]

REFUNDS = [
    {"order_id": 1041, "reason_code": "damaged", "amount_cents": 4500},
    {"order_id": 1077, "reason_code": "late", "amount_cents": 1200},
    {"order_id": 1093, "reason_code": "damaged", "amount_cents": 800},
]

STOCK = {
    "main": {"widget": 40, "gasket": 12},
    "annex": {"widget": 5},
}


def build_sales_report(year: int = 2026) -> dict:
    total = sum(row["amount_cents"] for row in SALES)
    return {"report": "sales", "year": year, "total_cents": total}


def build_refunds_report(year: int = 2026) -> dict:
    total = sum(row["amount_cents"] for row in REFUNDS)
    return {"report": "refunds", "year": year, "total_cents": total}


def build_inventory_report(warehouse: str = "main") -> dict:
    items = STOCK.get(warehouse, {})
    return {"report": "inventory", "warehouse": warehouse, "units": sum(items.values())}

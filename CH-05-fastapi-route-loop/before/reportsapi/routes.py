from fastapi import APIRouter

from reportsapi import reports

router = APIRouter()

# URL key -> name of the builder function in reports.py
REPORT_HANDLERS = {
    "sales": "build_sales_report",
    "refunds": "build_refunds_report",
    "inventory": "build_inventory_report",
}

for key, name in REPORT_HANDLERS.items():
    handler = getattr(reports, name)
    router.get(f"/reports/{key}")(handler)

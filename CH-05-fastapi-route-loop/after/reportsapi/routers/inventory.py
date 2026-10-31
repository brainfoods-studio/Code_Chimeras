from typing import Annotated

from fastapi import APIRouter, Query

from reportsapi.reports import build_inventory_report

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/inventory")
def inventory_report(warehouse: Annotated[str, Query(min_length=1)] = "main") -> dict:
    return build_inventory_report(warehouse)

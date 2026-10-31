from typing import Annotated

from fastapi import APIRouter, Query

from reportsapi.reports import build_sales_report

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/sales")
def sales_report(year: Annotated[int, Query(ge=2000)] = 2026) -> dict:
    return build_sales_report(year)

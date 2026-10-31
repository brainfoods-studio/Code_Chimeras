from typing import Annotated

from fastapi import APIRouter, Query

from reportsapi.reports import build_refunds_report

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/refunds")
def refunds_report(
    reason_code: Annotated[str, Query(min_length=1)],
    year: Annotated[int, Query(ge=2000)] = 2026,
) -> dict:
    return build_refunds_report(year, reason_code=reason_code)

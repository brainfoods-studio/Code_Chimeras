"""Calls the card gateway over HTTPS. The only module that talks to it."""
import json
import os
import urllib.request
from dataclasses import dataclass

GATEWAY_URL = "https://api.gateway.example/v1/charges"


@dataclass(frozen=True)
class ChargeResult:
    ok: bool
    charge_id: str
    decline_code: str = ""


def charge(customer_id: str, amount_cents: int, currency: str = "usd") -> ChargeResult:
    api_key = os.environ["PAYMENTS_API_KEY"]
    body = json.dumps(
        {"customer": customer_id, "amount": amount_cents, "currency": currency}
    ).encode()
    request = urllib.request.Request(
        GATEWAY_URL,
        data=body,
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.load(response)
    return ChargeResult(
        ok=data["status"] == "succeeded",
        charge_id=data["id"],
        decline_code=data.get("decline_code", ""),
    )

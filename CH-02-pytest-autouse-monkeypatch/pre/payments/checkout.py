from dataclasses import dataclass

from payments import client


class EmptyCartError(Exception):
    pass


@dataclass(frozen=True)
class Receipt:
    charge_id: str
    amount_cents: int


class PaymentDeclined(Exception):
    pass


def checkout(customer_id: str, line_amounts_cents: list[int]) -> Receipt:
    if not line_amounts_cents:
        raise EmptyCartError("cart is empty")
    total = sum(line_amounts_cents)
    result = client.charge(customer_id, total)
    if not result.ok:
        raise PaymentDeclined(result.decline_code)
    return Receipt(charge_id=result.charge_id, amount_cents=total)

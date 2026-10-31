from payments.gateway import ChargeResult


class FakeCharge:
    """Stands in for payments.checkout.charge and records each call."""

    def __init__(self) -> None:
        self.result = ChargeResult(ok=True, charge_id="ch_test")
        self.calls: list[tuple[str, int, str]] = []

    def __call__(
        self, customer_id: str, amount_cents: int, currency: str = "usd"
    ) -> ChargeResult:
        self.calls.append((customer_id, amount_cents, currency))
        return self.result

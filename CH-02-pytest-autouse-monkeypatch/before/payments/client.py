"""Kept so older imports of payments.client.charge keep working.

charge() moved to payments/gateway.py.
"""
from payments.gateway import ChargeResult, charge

__all__ = ["ChargeResult", "charge"]

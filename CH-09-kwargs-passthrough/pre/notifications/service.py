from typing import Any

from notifications.retry import send_with_retry


def notify(user: str, **opts: Any) -> str:
    return send_with_retry(user=user, **opts)

from typing import Any

from notifications.transport import TransportError, deliver

MAX_ATTEMPTS = 3


def send_with_retry(**kwargs: Any) -> str:
    last_error: TransportError | None = None
    for _ in range(MAX_ATTEMPTS):
        try:
            return deliver(**kwargs)
        except TransportError as error:
            last_error = error
    assert last_error is not None
    raise last_error

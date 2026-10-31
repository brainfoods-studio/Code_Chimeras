import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

from notifications.transport import TransportError, deliver

P = ParamSpec("P")
R = TypeVar("R")

MAX_ATTEMPTS = 3


def with_retry(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        last_error: TransportError | None = None
        for _ in range(MAX_ATTEMPTS):
            try:
                return func(*args, **kwargs)
            except TransportError as error:
                last_error = error
        assert last_error is not None
        raise last_error

    return wrapper


send_with_retry = with_retry(deliver)

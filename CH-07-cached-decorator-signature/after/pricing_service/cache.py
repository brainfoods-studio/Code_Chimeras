"""A small time-based cache decorator that keeps the decorated function's signature."""

import functools
import inspect
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def cached(ttl: float) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        signature = inspect.signature(func)
        store: dict[tuple, tuple[float, R]] = {}

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Bind to the real signature and fill in defaults, so a positional
            # argument, a keyword argument and a default all land on one key.
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            key = tuple(bound.arguments.items())
            now = time.monotonic()
            hit = store.get(key)
            if hit is not None and now - hit[0] < ttl:
                return hit[1]
            value = func(*args, **kwargs)
            store[key] = (now, value)
            return value

        return wrapper

    return decorator

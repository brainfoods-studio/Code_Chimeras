"""A small time-based cache decorator."""

import time


def cached(ttl):
    def decorator(func):
        store = {}

        def wrapper(*args, **kwargs):
            key = args
            now = time.monotonic()
            hit = store.get(key)
            if hit is not None and now - hit[0] < ttl:
                return hit[1]
            value = func(*args, **kwargs)
            store[key] = (now, value)
            return value

        return wrapper

    return decorator

class TransportError(Exception):
    pass


CHANNELS = ("email", "sms")


def deliver(user: str, channel: str = "email", *, template: str, locale: str = "en") -> str:
    if channel not in CHANNELS:
        raise TransportError(f"unknown channel {channel}")
    return f"{channel}:{user}:{template}:{locale}"

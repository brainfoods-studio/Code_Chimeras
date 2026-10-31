from notifications.retry import send_with_retry


def notify(user: str, channel: str = "email", *, template_id: str, locale: str = "en") -> str:
    return send_with_retry(user, channel, template_id=template_id, locale=locale)

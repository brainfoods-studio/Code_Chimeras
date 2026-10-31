from notifications.service import notify


def send_digest(user: str) -> str:
    return notify(user, channel="sms", template_id="digest", locale="de")

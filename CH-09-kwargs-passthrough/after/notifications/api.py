from notifications.service import notify


def welcome_user(user: str) -> str:
    return notify(user, template_id="welcome")


def send_receipt(user: str, locale: str) -> str:
    return notify(user, template_id="receipt", locale=locale)

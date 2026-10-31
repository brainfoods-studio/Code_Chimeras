import inspect

from notifications.api import send_receipt, welcome_user
from notifications.jobs import send_digest
from notifications.retry import send_with_retry


def test_receipt_uses_the_new_name():
    assert send_receipt("u1", "fr") == "email:u1:receipt:fr"


def test_welcome_user_sends_the_welcome_template():
    assert welcome_user("u1") == "email:u1:welcome:en"


def test_digest_job_sends_the_digest_template():
    assert send_digest("u1") == "sms:u1:digest:de"


def test_retry_wrapper_keeps_the_signature():
    assert send_with_retry.__name__ == "deliver"
    assert list(inspect.signature(send_with_retry).parameters) == ["user", "channel", "template_id", "locale"]

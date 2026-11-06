import pytest

from notifications.api import send_receipt, welcome_user
from notifications.jobs import send_digest


def test_receipt_sends_the_receipt_template():
    assert send_receipt("u1", "fr") == "email:u1:receipt:fr"


def test_welcome_user_sends_the_welcome_template():
    assert welcome_user("u1") == "email:u1:welcome:en"


def test_digest_job_sends_the_digest_template():
    assert send_digest("u1") == "sms:u1:digest:de"

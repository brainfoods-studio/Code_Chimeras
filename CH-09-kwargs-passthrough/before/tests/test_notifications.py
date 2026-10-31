import pytest

from notifications.api import send_receipt, welcome_user
from notifications.jobs import send_digest


def test_receipt_uses_the_new_name():
    assert send_receipt("u1", "fr") == "email:u1:receipt:fr"


# Written as it would be written; it fails as expected (xfail). deliver() in transport.py
# now takes template_id, but api.py and jobs.py still pass template=. notify(), then
# send_with_retry(), forward the keyword unchanged, so deliver() raises TypeError at the bottom.
@pytest.mark.xfail(strict=True, raises=TypeError, reason="api.py and jobs.py still pass template=, deliver() takes template_id")
def test_welcome_user_sends_the_welcome_template():
    assert welcome_user("u1") == "email:u1:welcome:en"


@pytest.mark.xfail(strict=True, raises=TypeError, reason="api.py and jobs.py still pass template=, deliver() takes template_id")
def test_digest_job_sends_the_digest_template():
    assert send_digest("u1") == "sms:u1:digest:de"

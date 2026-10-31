import pytest

from notifications.transport import TransportError, deliver


def test_deliver_defaults_to_email():
    assert deliver("u1", template_id="welcome") == "email:u1:welcome:en"


def test_deliver_takes_channel_and_locale():
    assert deliver("u1", "sms", template_id="digest", locale="de") == "sms:u1:digest:de"


def test_deliver_rejects_unknown_channel():
    with pytest.raises(TransportError):
        deliver("u1", "pager", template_id="welcome")

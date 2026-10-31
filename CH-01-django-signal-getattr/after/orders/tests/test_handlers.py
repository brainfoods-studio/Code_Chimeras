from django.core import mail
from django.test import TestCase

from orders import handlers
from orders.models import Order


class HandlerTests(TestCase):
    def setUp(self) -> None:
        # Created as "draft" so no handler runs before the test calls one.
        self.order = Order.objects.create(
            number="A-1001",
            customer_email="sam@example.com",
            total_cents=4250,
            status=Order.Status.DRAFT,
        )

    def test_on_placed_sends_confirmation(self) -> None:
        handlers.on_placed(self.order)
        self.assertEqual(mail.outbox[0].subject, "Order A-1001 received")

    def test_on_shipped_sends_tracking_notice(self) -> None:
        handlers.on_shipped(self.order)
        self.assertEqual(mail.outbox[0].subject, "Order A-1001 is on its way")

    def test_on_refunded_includes_reason(self) -> None:
        handlers.on_refunded(self.order, "damaged in transit")
        self.assertIn("damaged in transit", mail.outbox[0].body)

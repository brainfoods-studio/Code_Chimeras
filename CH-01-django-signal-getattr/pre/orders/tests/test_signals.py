from django.core import mail
from django.test import TestCase

from orders.models import Order


class SignalTests(TestCase):
    def test_placing_an_order_sends_confirmation(self) -> None:
        Order.objects.create(
            number="A-1002",
            customer_email="sam@example.com",
            total_cents=1999,
            status=Order.Status.PLACED,
        )
        self.assertEqual(mail.outbox[0].subject, "Order A-1002 received")

    def test_shipping_an_order_sends_tracking_notice(self) -> None:
        order = Order.objects.create(
            number="A-1003",
            customer_email="sam@example.com",
            total_cents=1999,
        )
        order.status = Order.Status.SHIPPED
        order.save()
        self.assertEqual(mail.outbox[-1].subject, "Order A-1003 is on its way")

    def test_refunding_an_order_sends_refund_notice(self) -> None:
        order = Order.objects.create(
            number="A-1004",
            customer_email="sam@example.com",
            total_cents=1999,
            status=Order.Status.PAID,
        )
        order.status = Order.Status.REFUNDED
        order.refund_reason = "damaged in transit"
        order.save()
        self.assertEqual(mail.outbox[-1].subject, "Refund issued for A-1004")

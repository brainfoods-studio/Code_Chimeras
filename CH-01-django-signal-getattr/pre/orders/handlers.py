"""What happens when an order reaches each status.

One function per status. The signal receiver in orders/signals.py picks one.
"""
from django.core.mail import send_mail

from orders.models import Order


def on_placed(order: Order) -> None:
    send_mail(
        subject=f"Order {order.number} received",
        message=f"We have your order for {order.total_cents / 100:.2f}.",
        from_email=None,
        recipient_list=[order.customer_email],
    )


def on_paid(order: Order) -> None:
    send_mail(
        subject=f"Payment received for {order.number}",
        message="Your payment went through. We are packing your order.",
        from_email=None,
        recipient_list=[order.customer_email],
    )


def on_shipped(order: Order) -> None:
    send_mail(
        subject=f"Order {order.number} is on its way",
        message="Your order has shipped.",
        from_email=None,
        recipient_list=[order.customer_email],
    )


def on_refunded(order: Order) -> None:
    send_mail(
        subject=f"Refund issued for {order.number}",
        message=f"We refunded {order.total_cents / 100:.2f}.",
        from_email=None,
        recipient_list=[order.customer_email],
    )

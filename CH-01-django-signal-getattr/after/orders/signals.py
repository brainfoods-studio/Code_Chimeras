from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from orders import handlers
from orders.models import Order


@receiver(post_save, sender=Order)
def dispatch_order_status(
    sender: type[Order], instance: Order, **kwargs: Any
) -> None:
    match instance.status:
        case Order.Status.PLACED:
            handlers.on_placed(instance)
        case Order.Status.PAID:
            handlers.on_paid(instance)
        case Order.Status.SHIPPED:
            handlers.on_shipped(instance)
        case Order.Status.REFUNDED:
            handlers.on_refunded(instance, instance.refund_reason)
        case _:
            pass  # draft: nothing to send

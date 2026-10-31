from django.db.models.signals import post_save
from django.dispatch import receiver

from orders import handlers
from orders.models import Order


@receiver(post_save)
def dispatch_order_status(sender, instance, **kwargs):
    if not isinstance(instance, Order):
        return
    handler = getattr(handlers, f"on_{instance.status}", None)
    if handler is not None:
        handler(instance)

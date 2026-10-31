from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = "orders"

    def ready(self) -> None:
        # Importing the module connects the @receiver functions in it.
        from orders import signals  # noqa: F401

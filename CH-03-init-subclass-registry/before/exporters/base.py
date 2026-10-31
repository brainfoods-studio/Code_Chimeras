"""Base class for exporters. A subclass that passes key="..." registers itself."""

REGISTRY = {}


class Exporter:
    def __init_subclass__(cls, key=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if key is not None:
            REGISTRY[key] = cls

    def export(self, rows):
        raise NotImplementedError

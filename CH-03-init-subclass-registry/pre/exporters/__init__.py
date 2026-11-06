from exporters.base import REGISTRY

# These imports exist for their side effect: each module defines a subclass
# of Exporter, and Exporter.__init_subclass__ adds it to REGISTRY.
from exporters import csv_exporter  # noqa: F401
from exporters import json_exporter  # noqa: F401
from exporters import xlsx_exporter  # noqa: F401

__all__ = ["REGISTRY"]

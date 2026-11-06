import json

from exporters.base import Exporter


class JsonExporter(Exporter, key="json"):
    def export(self, rows):
        return json.dumps(rows, sort_keys=True).encode("utf-8")

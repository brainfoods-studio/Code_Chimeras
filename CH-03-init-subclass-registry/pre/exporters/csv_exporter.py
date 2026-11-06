import csv
import io

from exporters.base import Exporter


class CsvExporter(Exporter, key="csv"):
    def export(self, rows):
        out = io.StringIO()
        if rows:
            writer = csv.DictWriter(out, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        return out.getvalue().encode("utf-8")

import csv
import io

from exporters.base import Exporter


class CsvExporter(Exporter, key="csv"):
    # Edit applied: encoding was added so one customer can get latin-1 files.
    # It used to be: def export(self, rows):
    def export(self, rows, *, encoding):
        out = io.StringIO()
        if rows:
            writer = csv.DictWriter(out, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        return out.getvalue().encode(encoding)

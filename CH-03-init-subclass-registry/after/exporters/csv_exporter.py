import csv
import io
from collections.abc import Sequence
from typing import ClassVar

from exporters.base import FormatKey, Row


class CsvExporter:
    key: ClassVar[FormatKey] = "csv"

    def __init__(self, encoding: str = "utf-8") -> None:
        self.encoding = encoding

    def export(self, rows: Sequence[Row]) -> bytes:
        out = io.StringIO()
        if rows:
            writer = csv.DictWriter(out, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        return out.getvalue().encode(self.encoding)

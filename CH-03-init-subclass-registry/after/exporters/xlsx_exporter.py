import io
from collections.abc import Sequence
from typing import ClassVar

from openpyxl import Workbook

from exporters.base import FormatKey, Row


class XlsxExporter:
    key: ClassVar[FormatKey] = "xlsx"

    def export(self, rows: Sequence[Row]) -> bytes:
        book = Workbook()
        sheet = book.active
        if rows:
            header = list(rows[0])
            sheet.append(header)
            for row in rows:
                sheet.append([row[name] for name in header])
        out = io.BytesIO()
        book.save(out)
        return out.getvalue()

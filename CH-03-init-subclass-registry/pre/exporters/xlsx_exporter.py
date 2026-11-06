import io

from openpyxl import Workbook

from exporters.base import Exporter


class XlsxExporter(Exporter, key="xlsx"):
    def export(self, rows):
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

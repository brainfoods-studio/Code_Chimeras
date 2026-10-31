from exporters.csv_exporter import CsvExporter
from exporters.json_exporter import JsonExporter

ROWS = [{"sku": "A-100", "qty": 3}, {"sku": "B-200", "qty": 1}]


def test_csv_exporter_writes_header_and_rows():
    data = CsvExporter().export(ROWS, encoding="utf-8")
    assert data.decode("utf-8").splitlines() == ["sku,qty", "A-100,3", "B-200,1"]


def test_csv_exporter_honours_encoding():
    rows = [{"name": "Zoë", "qty": 1}]
    assert "Zoë".encode("latin-1") in CsvExporter().export(rows, encoding="latin-1")


def test_json_exporter_round_trips():
    data = JsonExporter().export(ROWS)
    assert data == b'[{"qty": 3, "sku": "A-100"}, {"qty": 1, "sku": "B-200"}]'

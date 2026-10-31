import pytest

import cli
from exporters import REGISTRY, parse_format
from exporters.csv_exporter import CsvExporter

ROWS = [{"sku": "A-100", "qty": 3}, {"sku": "B-200", "qty": 1}]


def test_csv_exporter_honours_encoding():
    rows = [{"name": "Zoë", "qty": 1}]
    assert "Zoë".encode("latin-1") in CsvExporter(encoding="latin-1").export(rows)


@pytest.mark.parametrize("key", ["csv", "json", "xlsx"])
def test_every_format_key_has_an_exporter(key):
    assert REGISTRY[parse_format(key)].key == key


def test_cli_csv_format():
    assert cli.run("csv", ROWS).decode("utf-8").splitlines() == [
        "sku,qty",
        "A-100,3",
        "B-200,1",
    ]


def test_unknown_format_is_rejected():
    with pytest.raises(ValueError):
        parse_format("pdf")

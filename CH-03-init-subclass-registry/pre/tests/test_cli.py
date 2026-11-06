import pytest

import cli

ROWS = [{"sku": "A-100", "qty": 3}]


def test_cli_json_format():
    assert cli.run("json", ROWS) == b'[{"qty": 3, "sku": "A-100"}]'


def test_cli_csv_format():
    assert cli.run("csv", ROWS).decode("utf-8").splitlines() == ["sku,qty", "A-100,3"]

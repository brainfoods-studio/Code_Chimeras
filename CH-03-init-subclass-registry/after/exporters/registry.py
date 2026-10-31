from typing import get_args

from exporters.base import Exporter, FormatKey
from exporters.csv_exporter import CsvExporter
from exporters.json_exporter import JsonExporter
from exporters.xlsx_exporter import XlsxExporter

# The one place that says which formats exist. Adding a format is one edit here.
EXPORTER_CLASSES: tuple[type[Exporter], ...] = (
    CsvExporter,
    JsonExporter,
    XlsxExporter,
)

REGISTRY: dict[FormatKey, type[Exporter]] = {cls.key: cls for cls in EXPORTER_CLASSES}


def parse_format(value: str) -> FormatKey:
    for key in get_args(FormatKey):
        if value == key:
            return key
    raise ValueError(f"unknown format {value!r}; expected one of {get_args(FormatKey)}")

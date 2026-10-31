import json
from collections.abc import Sequence
from typing import ClassVar

from exporters.base import FormatKey, Row


class JsonExporter:
    key: ClassVar[FormatKey] = "json"

    def export(self, rows: Sequence[Row]) -> bytes:
        return json.dumps(rows, sort_keys=True).encode("utf-8")

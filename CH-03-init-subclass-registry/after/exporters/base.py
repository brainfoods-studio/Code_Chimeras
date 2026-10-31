from collections.abc import Mapping, Sequence
from typing import ClassVar, Literal, Protocol

FormatKey = Literal["csv", "json", "xlsx"]
Row = Mapping[str, object]


class Exporter(Protocol):
    """The contract every exporter meets. Settings go in __init__, not in export()."""

    key: ClassVar[FormatKey]

    def export(self, rows: Sequence[Row]) -> bytes: ...

import json
import sys
from collections.abc import Sequence

from exporters import REGISTRY, FormatKey, Row, parse_format


def run(fmt: FormatKey, rows: Sequence[Row]) -> bytes:
    return REGISTRY[fmt]().export(rows)


def main(argv: list[str]) -> int:
    fmt, path = parse_format(argv[1]), argv[2]
    with open(path, encoding="utf-8") as handle:
        rows = json.load(handle)
    sys.stdout.buffer.write(run(fmt, rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

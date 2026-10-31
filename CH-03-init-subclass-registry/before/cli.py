import json
import sys

from exporters import REGISTRY


def run(fmt, rows):
    return REGISTRY[fmt]().export(rows)


def main(argv):
    fmt, path = argv[1], argv[2]
    with open(path, encoding="utf-8") as handle:
        rows = json.load(handle)
    sys.stdout.buffer.write(run(fmt, rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

"""See a chimera break, then see the fix pass.

Usage:
    python reproduce.py CH-06
    python reproduce.py --list

It runs the chimera's tests on before/ (the edit is applied and one call is
left wrong; the run shows the break, as failing tests or as the test marked
xfail, expectedFailure or todo), then on after/ (the fix;
every test passes). Python 3.9 or later, standard library only.

What it runs is printed before it runs. For the Node chimeras it runs
`npm install` inside before/ and after/ (local node_modules only). For the
Python chimeras it installs nothing: install the packages listed under
"needs" first, ideally in a virtual environment.
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = [sys.executable, "-m", "pytest", "-rxX", "-q"]

CHIMERAS = {
    "CH-01": ("CH-01-django-signal-getattr", "python", ["django"],
              [[sys.executable, "manage.py", "test", "-v", "2"]],
              "before: the refund test is an expected failure (on_refunded is called without reason)"),
    "CH-02": ("CH-02-pytest-autouse-monkeypatch", "python", ["pytest"], [PY],
              "before: 2 checkout tests fail with KeyError inside gateway.py (the fixture patches an alias checkout no longer reads)"),
    "CH-03": ("CH-03-init-subclass-registry", "python", ["pytest", "openpyxl"], [PY],
              "before: the CSV CLI test is xfail (cli.py:8 calls export without encoding)"),
    "CH-04": ("CH-04-react-hoc-barrel", "node", [], [["npm", "test"], ["npm", "run", "typecheck"]],
              "before: tests and typecheck pass; the renamed prop never arrives (see the page, section 3)"),
    "CH-05": ("CH-05-fastapi-route-loop", "python", ["pytest", "fastapi", "httpx"], [PY],
              "before: GET /reports/refunds test is xfail (now 422)"),
    "CH-06": ("CH-06-express-computed-require", "node", [], [["npm", "test"]],
              "before: 1 todo test, /invoice/:id gets 404 (client/api.js:12 still uses the old prefix)"),
    "CH-07": ("CH-07-cached-decorator-signature", "python", ["pytest"], [PY],
              "before: the region test is xfail (the cache key ignores region)"),
    "CH-08": ("CH-08-string-event-emitter", "node", [], [["npm", "test"], ["npm", "run", "typecheck"]],
              "before: 1 todo test, the ledger stays empty (listeners wait for order:paid)"),
    "CH-09": ("CH-09-kwargs-passthrough", "python", ["pytest"], [PY],
              "before: 2 xfail tests, TypeError at retry.py:12 for the old template keyword"),
    "CH-11": ("CH-11-nextjs-dynamic-widgets", "node", [], [["npm", "test"], ["npm", "run", "typecheck"]],
              "before: 1 todo test, the config names Churn and no such widget file exists"),
}


def run(cmd, cwd):
    exe = shutil.which(cmd[0]) or cmd[0]
    print(f"\n$ (cd {cwd.relative_to(ROOT)}) {' '.join(cmd)}", flush=True)
    return subprocess.run([exe] + cmd[1:], cwd=cwd).returncode


def missing_python(mods):
    import importlib.util
    return [m for m in mods if importlib.util.find_spec(m) is None]


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--list":
        for key, (folder, *_rest) in CHIMERAS.items():
            print(f"{key}  {folder}")
        return 0
    key = argv[0].upper()
    if key not in CHIMERAS:
        print(f"Unknown chimera {argv[0]!r}. Try --list.")
        return 2
    folder, kind, needs, cmds, expect = CHIMERAS[key]
    base = ROOT / folder
    if kind == "python":
        gone = missing_python(needs)
        if gone:
            print(f"{key} needs these Python packages first: {' '.join(gone)}")
            print(f"  python -m pip install {' '.join(gone)}")
            return 2
    elif shutil.which("npm") is None:
        print(f"{key} needs Node.js with npm (Node 22 or later).")
        return 2

    codes = {}
    for side in ("before", "after"):
        print(f"\n===== {key} {side}/ =====")
        cwd = base / side
        if kind == "node" and run(["npm", "install", "--no-audit", "--no-fund"], cwd) != 0:
            print("npm install failed; see the output above.")
            return 1
        codes[side] = [run(c, cwd) for c in cmds]

    print(f"\n===== {key} summary =====")
    print(f"What to look for: {expect}")
    print("after: every test passes." if all(c == 0 for c in codes["after"])
          else "after: something failed; please open an issue with the output.")
    print(f"The page: https://beta.llmgraph.in/agent-readable/{key.lower()}/?ref=gh-reproduce")
    return 0 if all(c == 0 for c in codes["after"]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

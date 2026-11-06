# Why do my pytest tests pass for a reason I can't see?

An autouse fixture in `conftest.py` replaces a function for every test, and no test mentions it. When an ordinary refactor moves that function, the fixture can keep succeeding while it patches a name the code no longer looks up, and the tests fail somewhere else with a traceback that never touches the test file. Name the fixture, request it in the tests that need it, and patch the module that does the lookup.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-02/?ref=gh-chimeras

## Rules that apply

- **AR-18**: no monkeypatching in production code; in tests, patch through the fixture and mock API at the import site.
- **AR-34**: fixtures in the nearest `conftest.py`, named for what they return, with no autouse for behaviour changes. `fake_charge` returns the fake; the old `_no_real_charges` named an intent and changed behaviour.
- **AR-35**: patch where the name is looked up, through `monkeypatch` or `mocker`, never by reassigning module globals.

## Run the tests

Python with pytest installed. Run the commands in `before/` to see the break, then in `after/` to see the fix.

`pre/` is the project before the edit; `edit.patch` is the edit (pre/ to before/).

```
cd before   # or: cd after
pytest
```

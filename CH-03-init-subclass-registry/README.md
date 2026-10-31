# Why did my plugin registry lose a format after an edit?

A base class registers every subclass in `__init_subclass__`, a package `__init__.py` imports the submodules so the registration runs, and the CLI looks the class up by a string key. It is compact, and adding a format is one new file. It also means the list of formats and the signature of the call live in places nobody reads together. Build the registry in one module from a literal tuple of classes, give the exporters a `Protocol`, and type the keys with `Literal`.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-03/?ref=gh-chimeras

## Rules that apply

- **AR-06**: keep import side effects out of modules; registration happens in an explicit setup call. In `after/` the registry is built by ordinary code in one module.
- **AR-09**: for open sets, register explicitly into a typed registry next to a typed contract.
- **AR-21**: keep `__init_subclass__` generation out of edit paths; when you use it, document what it generates.

## Run the tests

Python with pytest installed. The page also checks types with pyright. Run the commands in `before/` to see the break, then in `after/` to see the fix.

```
cd before   # or: cd after
pytest
pyright
```

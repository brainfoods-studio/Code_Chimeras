# Why does my renamed keyword argument fail at runtime?

A service function takes `**opts`, hands it to a retry helper, and the helper hands it to the function that does the work. Each layer is a few lines and none of them names a parameter. Rename a keyword on the bottom function and every layer above still accepts the old one, so the failure waits for a `TypeError` at the bottom call. Spell the parameters at the layer callers use, and give the retry wrapper a `ParamSpec` type so it carries the callee's signature.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-09/?ref=gh-chimeras

## Rules that apply

- **AR-11**: avoid `**kwargs` pass-through layers that hide the real signature; spell the parameters or use `ParamSpec`. A thin adapter that must forward everything keeps its generic shape by typing it with `ParamSpec`, and a public entry point spells its parameters.

## Run the tests

Python 3.12 with pytest. Run the commands in `before/` to see the break, then in `after/` to see the fix. The page also reports mypy and pyright on both folders.

```
cd before   # or: cd after
pytest
mypy .        # optional
pyright       # optional
```

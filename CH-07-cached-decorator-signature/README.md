# Why does my cached function return the wrong value?

A caching decorator replaces the function it wraps with its own `wrapper(*args, **kwargs)`. Callers now hold the wrapper, so the real parameter list is gone at runtime and for mypy, and a cache key built from `args` alone ignores keyword arguments. Add one keyword to the decorated function and two different calls can share one cached answer. Wrap with `functools.wraps`, type the decorator with `ParamSpec`, and build the key from the bound, defaulted arguments.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-07/?ref=gh-chimeras

## Rules that apply

- **AR-12**: use `functools.wraps` and preserve signatures in decorators. A decorator that changes the shape on purpose should say so in its type; this one does not, so it should return the same shape it was given.

## Run the tests

Python with pytest installed. Run the commands in `before/` to see the break, then in `after/` to see the fix.

`pre/` is the project before the edit; `edit.patch` is the edit (pre/ to before/).

```
cd before   # or: cd after
pytest
```

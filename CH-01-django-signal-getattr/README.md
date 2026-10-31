# Why does my Django signal break after a refactor?

An order's status field decides which handler runs: a `post_save` receiver builds the function name from the status and calls it through `getattr`. Tests that call the handlers directly keep passing when a handler's signature changes, because the call that went wrong is a string-built name that no test and no type checker connects to the handler. Replace the lookup with an explicit `match` and the call is an ordinary call again.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-01/?ref=gh-chimeras

## Rules that apply

- **AR-07**: don't build method names as strings.
- **AR-08**: dispatch over a closed set with a literal-keyed mapping or an explicit `match`. The order status is a closed set.
- **AR-31**: Django signals get an explicit `sender` and live in one `signals.py` per app, imported in `AppConfig.ready()`.
- **AR-25**: before changing a signature, list every caller and every dynamic site that might reach it. The `getattr` site is the one a plain search won't list.

## Run the tests

Python with Django installed (the example uses the Django test runner and an in-memory test database). Run the commands in `before/` to see the break, then in `after/` to see the fix.

```
cd before   # or: cd after
python manage.py test
```

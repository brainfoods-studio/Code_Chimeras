# Why did my FastAPI route start returning 422?

A loop reads a dict of URL keys and function names, looks each function up with `getattr`, and registers it as a route. FastAPI then builds the URL's query parameters from that function's signature, so a signature edit in the reports module changes the public URL without touching the routes file. Write each route as a decorated function on an `APIRouter`, declare its query parameters with `Annotated`, and include the routers by name.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-05/?ref=gh-chimeras

## Rules that apply

- **AR-08**: dispatch over a closed set should be written so a checker can follow it. A dict of function names handed to `getattr` is a table the checker cannot read; a decorated function per route is a direct name.
- **AR-33**: routes are decorated functions on an `APIRouter`, included by name in `main.py`. Do not build routes in loops from strings.

## Run the tests

Python with pytest installed. Run the commands in `before/` to see the break, then in `after/` to see the fix.

```
cd before   # or: cd after
pytest
```

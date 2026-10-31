# Code Chimeras: example code for the Agent Rules rulebook

These are the small example projects behind the chimera pages of the [Agent Rules rulebook](https://beta.llmgraph.in/agent-readable/?ref=gh-chimeras). Each folder has the code before and after the fix, and the tests that show the break.

| Chimera | Title | Framework | Rules | Page | Folder |
| --- | --- | --- | --- | --- | --- |
| CH-01 | Why does my Django signal break after a refactor? | Django | [AR-07](https://beta.llmgraph.in/agent-readable/ar-07/), [AR-08](https://beta.llmgraph.in/agent-readable/ar-08/), [AR-25](https://beta.llmgraph.in/agent-readable/ar-25/), [AR-31](https://beta.llmgraph.in/agent-readable/ar-31/) | [page](https://beta.llmgraph.in/agent-readable/ch-01/?ref=gh-chimeras) | [CH-01-django-signal-getattr](CH-01-django-signal-getattr/) |
| CH-02 | Why do my pytest tests pass for a reason I can't see? | pytest | [AR-18](https://beta.llmgraph.in/agent-readable/ar-18/), [AR-34](https://beta.llmgraph.in/agent-readable/ar-34/), [AR-35](https://beta.llmgraph.in/agent-readable/ar-35/) | [page](https://beta.llmgraph.in/agent-readable/ch-02/?ref=gh-chimeras) | [CH-02-pytest-autouse-monkeypatch](CH-02-pytest-autouse-monkeypatch/) |
| CH-03 | Why did my plugin registry lose a format after an edit? | Python (__init_subclass__ registry) | [AR-06](https://beta.llmgraph.in/agent-readable/ar-06/), [AR-09](https://beta.llmgraph.in/agent-readable/ar-09/), [AR-21](https://beta.llmgraph.in/agent-readable/ar-21/) | [page](https://beta.llmgraph.in/agent-readable/ch-03/?ref=gh-chimeras) | [CH-03-init-subclass-registry](CH-03-init-subclass-registry/) |
| CH-04 | Why does a React prop stop arriving after a rename? | React (higher-order component, barrel) | [AR-02](https://beta.llmgraph.in/agent-readable/ar-02/), [AR-36](https://beta.llmgraph.in/agent-readable/ar-36/) | [page](https://beta.llmgraph.in/agent-readable/ch-04/?ref=gh-chimeras) | [CH-04-react-hoc-barrel](CH-04-react-hoc-barrel/) |
| CH-05 | Why did my FastAPI route start returning 422? | FastAPI | [AR-08](https://beta.llmgraph.in/agent-readable/ar-08/), [AR-33](https://beta.llmgraph.in/agent-readable/ar-33/) | [page](https://beta.llmgraph.in/agent-readable/ch-05/?ref=gh-chimeras) | [CH-05-fastapi-route-loop](CH-05-fastapi-route-loop/) |
| CH-06 | Why did renaming an Express route file break my client? | Express (Node, CommonJS) | [AR-37](https://beta.llmgraph.in/agent-readable/ar-37/), [AR-38](https://beta.llmgraph.in/agent-readable/ar-38/) | [page](https://beta.llmgraph.in/agent-readable/ch-06/?ref=gh-chimeras) | [CH-06-express-computed-require](CH-06-express-computed-require/) |
| CH-07 | Why does my cached function return the wrong value? | Python decorators | [AR-12](https://beta.llmgraph.in/agent-readable/ar-12/) | [page](https://beta.llmgraph.in/agent-readable/ch-07/?ref=gh-chimeras) | [CH-07-cached-decorator-signature](CH-07-cached-decorator-signature/) |
| CH-08 | Why did my event listener stop firing? | Node EventEmitter, TypeScript | [AR-13](https://beta.llmgraph.in/agent-readable/ar-13/), [AR-39](https://beta.llmgraph.in/agent-readable/ar-39/) | [page](https://beta.llmgraph.in/agent-readable/ch-08/?ref=gh-chimeras) | [CH-08-string-event-emitter](CH-08-string-event-emitter/) |
| CH-09 | Why does my renamed keyword argument fail at runtime? | Python typing | [AR-11](https://beta.llmgraph.in/agent-readable/ar-11/) | [page](https://beta.llmgraph.in/agent-readable/ch-09/?ref=gh-chimeras) | [CH-09-kwargs-passthrough](CH-09-kwargs-passthrough/) |
| CH-11 | Why does my Next.js widget fail to load after a rename? | Next.js, TypeScript | [AR-37](https://beta.llmgraph.in/agent-readable/ar-37/) | [page](https://beta.llmgraph.in/agent-readable/ch-11/?ref=gh-chimeras) | [CH-11-nextjs-dynamic-widgets](CH-11-nextjs-dynamic-widgets/) |

## Run the tests

Run these inside the `before/` or `after/` directory of a folder. Each folder README has the same commands.

- CH-01 (Django): `python manage.py test`
- CH-02 (pytest): `pytest`
- CH-03 (Python): `pytest`, and `pyright` for the type check
- CH-04 (React): `npm install`, then `npm run typecheck` (tsc --noEmit) and `npm test` (vitest run)
- CH-05 (FastAPI): `pytest`
- CH-06 (Express): `npm install`, then `npm test` (node --test)
- CH-07 (Python decorators): `pytest`
- CH-08 (Node EventEmitter): `npm install`, then `npm test` (node --test) and `npm run typecheck` (tsc --noEmit)
- CH-09 (Python typing): `pytest` (mypy and pyright optional)
- CH-11 (Next.js): `npm install`, then `npm test` (node --test) and `npm run typecheck` (tsc --noEmit)

Related: the lint preset that enforces these rules: https://github.com/brainfoods-studio/agent-readable

## Licence

MIT. See [LICENSE](LICENSE).

---

Made by Brainfoods Studio, the team behind LLMGRAPH (https://beta.llmgraph.in/?ref=gh-chimeras).

# Why does my Next.js widget fail to load after a rename?

A dashboard page keeps its widgets in a config list and loads each one with ``dynamic(() => import(`../widgets/${name}`))``. The file name lives in the config as a string, and the import path is built from it when the slot renders. Rename `widgets/Churn.tsx` and no import in the project names it, so the rename has no importer to update and the slot fails when it loads. Write one literal `import()` per widget in a table keyed by a union of string literals, and type the config with that union.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-11/?ref=gh-chimeras

## Rules that apply

- **AR-37**: in React and Next.js, don't call `import()` with a computed path for components agents edit. Keep one literal import per component, in a table keyed by a literal union.

## Run the tests

Node 24 with npm. Run the commands in `before/` to see the break, then in `after/` to see the fix.

`pre/` is the project before the edit; `edit.patch` is the edit (pre/ to before/).

```
cd before   # or: cd after
npm install
npm test             # node --test "tests/*.test.ts"
npm run typecheck   # tsc --noEmit
```

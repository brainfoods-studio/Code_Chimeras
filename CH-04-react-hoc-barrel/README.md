# Why does a React prop stop arriving after a rename?

A higher-order component injects a handler prop, the wrapped components are re-exported through `export *`, and pages import the wrapped version from the barrel. The component file shows a prop that nothing in that file supplies, and the page shows no prop at all. Use a hook inside each component, re-export by name, and give the payload a type.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-04/?ref=gh-chimeras

## Rules that apply

- **AR-02**: re-export through an explicit list, not `export *` chains.
- **AR-36**: in React, prefer hooks and explicit props over higher-order components that inject props.

## Run the tests

Node with npm. Run the commands in `before/` to see the break, then in `after/` to see the fix.

`pre/` is the project before the edit; `edit.patch` is the edit (pre/ to before/).

```
cd before   # or: cd after
npm install
npm run typecheck   # tsc --noEmit
npm test             # vitest run
```

# Why did my event listener stop firing?

An order service announces a paid order with `bus.emit("order:paid", order)`. A receipt module and a ledger module each listen for the same string and read the payload as `any`. The event name is a plain string and the payload is untyped, so renaming either one in the emitter leaves the listeners in other files unchanged, and the compiler has nothing to compare them with. Declare the event names and payload types once in an interface, and put a small typed `emit` and `on` in front of the emitter.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-08/?ref=gh-chimeras

## Rules that apply

- **AR-13**: annotate public function parameters and returns, and use `any` only at a documented boundary. The listener parameter was `any` in the middle of the service, and now it is `Order`.
- **AR-39**: declare event names as a typed union or map with typed payloads. Do not emit free strings with `any` arguments.

## Run the tests

Node 24 with npm. Run the commands in `before/` to see the break, then in `after/` to see the fix.

`pre/` is the project before the edit; `edit.patch` is the edit (pre/ to before/).

```
cd before   # or: cd after
npm install
npm test             # node --test "tests/*.test.ts"
npm run typecheck   # tsc --noEmit
```

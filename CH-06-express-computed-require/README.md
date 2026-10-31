# Why did renaming an Express route file break my client?

`app.js` lists the `routes/` directory, requires each file by a path it builds at startup, and mounts the router under a prefix taken from the file name. The file name is now a public URL, and nothing in the source names that URL. Rename `invoice.js` to `invoices.js` and the API moves to a new path while the client keeps calling the old one. Write an explicit route table that imports each router by a literal path and mounts it with a literal prefix.

Read the full walkthrough: https://beta.llmgraph.in/agent-readable/ch-06/?ref=gh-chimeras

## Rules that apply

- **AR-37**: do not load files with a computed path where an agent edits them. `require("./routes/" + file)` is the CommonJS form of the dynamic import in that rule.
- **AR-38**: register routes and middleware explicitly in one router module, with a literal import and a literal prefix per router.

## Run the tests

Node 24 with npm. Run the commands in `before/` to see the break, then in `after/` to see the fix.

```
cd before   # or: cd after
npm install
npm test   # node --test tests/
```

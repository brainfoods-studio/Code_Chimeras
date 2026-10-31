const test = require("node:test");
const assert = require("node:assert");

const app = require("../app");

async function withServer(run) {
  const server = app.listen(0);
  try {
    await run("http://127.0.0.1:" + server.address().port);
  } finally {
    server.close();
  }
}

test("GET /customers/1 returns the customer", () =>
  withServer(async (base) => {
    const response = await fetch(base + "/customers/1");
    assert.strictEqual(response.status, 200);
    assert.strictEqual((await response.json()).name, "Harbor Print Co.");
  }));

test("GET /invoices/501 returns the invoice", () =>
  withServer(async (base) => {
    const response = await fetch(base + "/invoices/501");
    assert.strictEqual(response.status, 200);
    assert.strictEqual((await response.json()).totalCents, 12900);
  }));

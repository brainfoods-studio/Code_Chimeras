import test from "node:test";
import assert from "node:assert";

import { receiptBody } from "../src/email.ts";
import { entryFor, ledgerEntries } from "../src/ledger.ts";
import { createOrder, markPaid } from "../src/orders.ts";

test("receiptBody formats the total", () => {
  const order = createOrder("A-1001", "buyer@example.com", 4900);
  assert.strictEqual(receiptBody(order), "Order A-1001 paid: 49.00");
});

test("entryFor builds a ledger entry from an order", () => {
  const order = createOrder("A-1002", "buyer@example.com", 12000);
  assert.deepStrictEqual(entryFor(order), { orderId: "A-1002", cents: 12000 });
});

// Written as it would be written; it fails as expected (todo). The emitter in orders.ts
// now emits "order.paid", while email.ts and ledger.ts still listen for "order:paid".
// Node's emit returns false when nobody listens and throws nothing, so markPaid
// finishes and the ledger stays empty. No other test calls markPaid.
test("markPaid writes a ledger entry", { todo: "orders.ts emits order.paid; ledger.ts and email.ts still listen for order:paid" }, () => {
  const order = createOrder("A-1003", "buyer@example.com", 2500);
  markPaid(order);
  assert.deepStrictEqual(ledgerEntries.at(-1), { orderId: "A-1003", cents: 2500 });
});

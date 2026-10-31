import test from "node:test";
import assert from "node:assert";

import { receiptBody, sentReceipts } from "../src/email.ts";
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

test("markPaid writes a ledger entry", () => {
  const order = createOrder("A-1003", "buyer@example.com", 2500);
  markPaid(order);
  assert.deepStrictEqual(ledgerEntries.at(-1), { orderId: "A-1003", cents: 2500 });
});

test("markPaid sends a receipt", () => {
  const order = createOrder("A-1004", "buyer@example.com", 1800);
  markPaid(order);
  assert.deepStrictEqual(sentReceipts.at(-1), { to: "buyer@example.com", body: "Order A-1004 paid: 18.00" });
});

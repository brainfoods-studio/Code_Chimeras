const test = require("node:test");
const assert = require("node:assert");

const { getInvoice } = require("../services/invoices");
const { getCustomer } = require("../services/customers");

test("getInvoice returns the invoice with its total", () => {
  assert.deepStrictEqual(getInvoice(501), { id: 501, customerId: 1, totalCents: 12900 });
});

test("getInvoice returns null for an unknown id", () => {
  assert.strictEqual(getInvoice(999), null);
});

test("getCustomer finds a customer by id", () => {
  assert.strictEqual(getCustomer(2).name, "Linden Bakery");
});

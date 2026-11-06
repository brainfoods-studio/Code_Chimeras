import test from "node:test";
import assert from "node:assert";

import { formatCents, churnRate, signupsPerDay } from "../lib/metrics.ts";

test("formatCents shows two decimals", () => {
  assert.strictEqual(formatCents(1234567), "12345.67");
});

test("churnRate is the share of customers lost", () => {
  assert.strictEqual(churnRate(200, 10), 0.05);
});

test("signupsPerDay rounds to a whole number", () => {
  assert.strictEqual(signupsPerDay(930, 30), 31);
});

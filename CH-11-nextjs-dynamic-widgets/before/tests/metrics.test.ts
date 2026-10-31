import test from "node:test";
import assert from "node:assert";

import { formatCents, retentionRate, signupsPerDay } from "../lib/metrics.ts";

test("formatCents shows two decimals", () => {
  assert.strictEqual(formatCents(1234567), "12345.67");
});

test("retentionRate is the share of customers kept", () => {
  assert.strictEqual(retentionRate(200, 10), 0.95);
});

test("signupsPerDay rounds to a whole number", () => {
  assert.strictEqual(signupsPerDay(930, 30), 31);
});

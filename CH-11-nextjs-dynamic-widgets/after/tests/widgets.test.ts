import test from "node:test";
import assert from "node:assert";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

import { DASHBOARD_WIDGETS } from "../app/dashboard/widgets.config.ts";
import { WIDGET_KEYS } from "../widgets/keys.ts";

const root = join(import.meta.dirname, "..");
const slotSource = readFileSync(join(root, "components", "WidgetSlot.tsx"), "utf8");

// These tests read the lookup table in WidgetSlot.tsx as text, because loading it
// would need Next itself. They check the literal import in each entry and the file behind it.
test("every widget key has a literal import of a file that exists", () => {
  for (const key of WIDGET_KEYS) {
    const entry = new RegExp(String.raw`${key}: dynamic\(\(\) => import\("\.\./widgets/(\w+)"\)\)`).exec(slotSource);
    assert.ok(entry, `no literal import for ${key} in WidgetSlot.tsx`);
    assert.ok(existsSync(join(root, "widgets", `${entry[1]}.tsx`)), `widgets/${entry[1]}.tsx does not exist`);
  }
});

test("WidgetSlot builds no import path from a variable", () => {
  assert.ok(!/import\(`/.test(slotSource));
});

test("every configured widget is a known key", () => {
  for (const name of DASHBOARD_WIDGETS) {
    assert.ok((WIDGET_KEYS as readonly string[]).includes(name), `${name} is not a widget key`);
  }
});

import test from "node:test";
import assert from "node:assert";
import { existsSync } from "node:fs";
import { join } from "node:path";

import { DASHBOARD_WIDGETS } from "../app/dashboard/widgets.config.ts";

const widgetsDir = join(import.meta.dirname, "..", "widgets");

test("every configured widget has a file in widgets/", () => {
  for (const name of DASHBOARD_WIDGETS) {
    assert.ok(existsSync(join(widgetsDir, `${name}.tsx`)), `widgets/${name}.tsx does not exist`);
  }
});

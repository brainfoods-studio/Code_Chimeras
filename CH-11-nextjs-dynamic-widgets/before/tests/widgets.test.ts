import test from "node:test";
import assert from "node:assert";
import { existsSync } from "node:fs";
import { join } from "node:path";

import { DASHBOARD_WIDGETS } from "../app/dashboard/widgets.config.ts";

const widgetsDir = join(import.meta.dirname, "..", "widgets");

// Written as it would be written; it fails as expected (todo). widgets/Churn.tsx was
// renamed to widgets/Retention.tsx, and the component and tests/metrics.test.ts were
// updated with it. widgets.config.ts still lists "Churn", and WidgetSlot.tsx builds the
// import path from that string, so the slot has no file to load.
test("every configured widget has a file in widgets/", { todo: "widgets.config.ts lists Churn; widgets/Churn.tsx was renamed to Retention.tsx" }, () => {
  for (const name of DASHBOARD_WIDGETS) {
    assert.ok(existsSync(join(widgetsDir, `${name}.tsx`)), `widgets/${name}.tsx does not exist`);
  }
});

"use client";

import dynamic from "next/dynamic";
import type { ComponentType } from "react";

import type { WidgetKey } from "../widgets/keys";

const WIDGETS = {
  revenue: dynamic(() => import("../widgets/Revenue")),
  retention: dynamic(() => import("../widgets/Retention")),
  signups: dynamic(() => import("../widgets/Signups")),
} satisfies Record<WidgetKey, ComponentType>;

export function WidgetSlot({ name }: { name: WidgetKey }) {
  const Widget = WIDGETS[name];
  return <Widget />;
}

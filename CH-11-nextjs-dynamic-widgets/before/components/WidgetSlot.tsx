"use client";

import dynamic from "next/dynamic";

export function WidgetSlot({ name }: { name: string }) {
  const Widget = dynamic(() => import(`../widgets/${name}`));
  return <Widget />;
}

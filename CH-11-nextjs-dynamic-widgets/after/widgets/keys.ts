export const WIDGET_KEYS = ["revenue", "retention", "signups"] as const;

export type WidgetKey = (typeof WIDGET_KEYS)[number];

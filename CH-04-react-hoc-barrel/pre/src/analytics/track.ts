export type TrackPayload = Record<string, unknown>;

export function track(event: { component: string } & TrackPayload): void {
  navigator.sendBeacon("/api/events", JSON.stringify(event));
}

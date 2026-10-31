import type { ComponentType } from "react";
import { track, type TrackPayload } from "../analytics/track";

export type TrackFn = (payload: TrackPayload) => void;

export function withTracking<P extends object>(
  Component: ComponentType<P & { onEvent?: TrackFn }>,
) {
  function Tracked(props: P) {
    const name = Component.displayName ?? Component.name;
    const onTrack: TrackFn = (payload) => track({ component: name, ...payload });
    // Edit applied: the injected prop was renamed from onTrack to onEvent (lines 7 and 13).
    return <Component {...(props as P)} onEvent={onTrack} />;
  }
  Tracked.displayName = `withTracking(${Component.displayName ?? Component.name})`;
  return Tracked;
}

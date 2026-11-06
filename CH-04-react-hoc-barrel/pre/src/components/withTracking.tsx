import type { ComponentType } from "react";
import { track, type TrackPayload } from "../analytics/track";

export type TrackFn = (payload: TrackPayload) => void;

export function withTracking<P extends object>(
  Component: ComponentType<P & { onTrack?: TrackFn }>,
) {
  function Tracked(props: P) {
    const name = Component.displayName ?? Component.name;
    const onTrack: TrackFn = (payload) => track({ component: name, ...payload });
    return <Component {...(props as P)} onTrack={onTrack} />;
  }
  Tracked.displayName = `withTracking(${Component.displayName ?? Component.name})`;
  return Tracked;
}

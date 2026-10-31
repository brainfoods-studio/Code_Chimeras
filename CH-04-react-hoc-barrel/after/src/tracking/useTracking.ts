import { useContext } from "react";
import type { TrackFn } from "./events";
import { TrackingContext } from "./TrackingContext";

export function useTracking(component: string): { track: TrackFn } {
  const sink = useContext(TrackingContext);
  return { track: (payload) => sink({ component, ...payload }) };
}

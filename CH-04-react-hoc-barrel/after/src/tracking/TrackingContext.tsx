import { createContext, type ReactNode } from "react";
import type { TrackFn } from "./events";

export type TrackSink = (event: { component: string } & Parameters<TrackFn>[0]) => void;

const sendBeacon: TrackSink = (event) => {
  navigator.sendBeacon("/api/events", JSON.stringify(event));
};

export const TrackingContext = createContext<TrackSink>(sendBeacon);

export function TrackingProvider({ sink, children }: { sink: TrackSink; children: ReactNode }) {
  return <TrackingContext.Provider value={sink}>{children}</TrackingContext.Provider>;
}

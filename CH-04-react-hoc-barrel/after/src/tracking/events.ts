export type TrackPayload =
  | { action: "select_plan"; label: string; value: number }
  | { action: "signup_click"; label: string };

export type TrackFn = (payload: TrackPayload) => void;

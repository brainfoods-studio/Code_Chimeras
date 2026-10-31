import { withTracking, type TrackFn } from "./withTracking";

type Props = {
  plan: string;
  priceCents: number;
  onTrack?: TrackFn;
};

export function PriceCardBase({ plan, priceCents, onTrack }: Props) {
  return (
    <button
      onClick={() => onTrack?.({ action: "select_plan", label: plan, value: priceCents })}
    >
      {plan}: ${(priceCents / 100).toFixed(2)}
    </button>
  );
}

export const PriceCard = withTracking(PriceCardBase);

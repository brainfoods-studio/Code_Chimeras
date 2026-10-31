import { useTracking } from "../tracking/useTracking";

export type PriceCardProps = {
  plan: string;
  priceCents: number;
};

export function PriceCard({ plan, priceCents }: PriceCardProps) {
  const { track } = useTracking("PriceCard");
  return (
    <button onClick={() => track({ action: "select_plan", label: plan, value: priceCents })}>
      {plan}: ${(priceCents / 100).toFixed(2)}
    </button>
  );
}

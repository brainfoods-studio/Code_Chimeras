import { PriceCard, SignupButton } from "../components";

export function Pricing() {
  return (
    <main>
      <PriceCard plan="Solo" priceCents={900} />
      <PriceCard plan="Team" priceCents={2900} />
      <SignupButton source="pricing" />
    </main>
  );
}

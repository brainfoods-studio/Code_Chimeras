import { churnRate } from "../lib/metrics";

export default function Churn() {
  return (
    <section>
      <h2>Churn</h2>
      <p>{churnRate(200, 10)}</p>
    </section>
  );
}

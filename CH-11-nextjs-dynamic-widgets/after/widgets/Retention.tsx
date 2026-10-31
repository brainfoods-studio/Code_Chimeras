import { retentionRate } from "../lib/metrics";

export default function Retention() {
  return (
    <section>
      <h2>Retention</h2>
      <p>{retentionRate(200, 10)}</p>
    </section>
  );
}

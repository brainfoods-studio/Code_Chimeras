import { formatCents } from "../lib/metrics";

export default function Revenue() {
  return (
    <section>
      <h2>Revenue</h2>
      <p>{formatCents(1234567)}</p>
    </section>
  );
}

import { signupsPerDay } from "../lib/metrics";

export default function Signups() {
  return (
    <section>
      <h2>Signups</h2>
      <p>{signupsPerDay(930, 30)} per day</p>
    </section>
  );
}

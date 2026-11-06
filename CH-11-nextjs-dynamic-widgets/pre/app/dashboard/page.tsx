import { WidgetSlot } from "../../components/WidgetSlot";
import { DASHBOARD_WIDGETS } from "./widgets.config";

export default function DashboardPage() {
  return (
    <main>
      <h1>Dashboard</h1>
      {DASHBOARD_WIDGETS.map((name) => (
        <WidgetSlot key={name} name={name} />
      ))}
    </main>
  );
}

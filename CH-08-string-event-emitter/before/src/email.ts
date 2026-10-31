import { bus } from "./bus.ts";
import type { Order } from "./orders.ts";

export const sentReceipts: { to: string; body: string }[] = [];

export function receiptBody(order: Order): string {
  return `Order ${order.id} paid: ${(order.totalCents / 100).toFixed(2)}`;
}

bus.on("order:paid", (o: any) => {
  sentReceipts.push({ to: o.customerEmail, body: receiptBody(o) });
});

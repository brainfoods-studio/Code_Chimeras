import { bus } from "./bus.ts";
import type { Order } from "./types.ts";

export function createOrder(id: string, customerEmail: string, totalCents: number): Order {
  return { id, customerEmail, totalCents };
}

export function markPaid(order: Order): void {
  bus.emit("order:paid", order);
}

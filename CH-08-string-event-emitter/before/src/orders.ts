import { bus } from "./bus.ts";

export interface Order {
  id: string;
  customerEmail: string;
  totalCents: number;
}

export function createOrder(id: string, customerEmail: string, totalCents: number): Order {
  return { id, customerEmail, totalCents };
}

export function markPaid(order: Order): void {
  bus.emit("order.paid", order);
}

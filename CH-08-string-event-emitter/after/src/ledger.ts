import { bus } from "./bus.ts";
import type { Order } from "./types.ts";

export interface LedgerEntry {
  orderId: string;
  cents: number;
}

export const ledgerEntries: LedgerEntry[] = [];

export function entryFor(order: Order): LedgerEntry {
  return { orderId: order.id, cents: order.totalCents };
}

bus.on("order:paid", (order) => {
  ledgerEntries.push(entryFor(order));
});

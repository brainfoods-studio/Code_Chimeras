import { EventEmitter } from "node:events";

import type { Order } from "./types.ts";

// Every event name and its payload type, in one place.
export interface OrderEvents {
  "order:paid": Order;
}

class TypedBus<Events> {
  #emitter = new EventEmitter();

  emit<K extends keyof Events & string>(name: K, payload: Events[K]): boolean {
    return this.#emitter.emit(name, payload);
  }

  on<K extends keyof Events & string>(name: K, listener: (payload: Events[K]) => void): this {
    this.#emitter.on(name, listener);
    return this;
  }
}

export const bus = new TypedBus<OrderEvents>();

import { fireEvent, render, screen } from "@testing-library/react";
import { expect, test, vi } from "vitest";
import { PriceCardBase } from "./PriceCard";

test("clicking a plan reports select_plan with the plan name and price", () => {
  const onTrack = vi.fn();
  render(<PriceCardBase plan="Solo" priceCents={900} onTrack={onTrack} />);
  fireEvent.click(screen.getByRole("button"));
  expect(onTrack).toHaveBeenCalledWith({ action: "select_plan", label: "Solo", value: 900 });
});

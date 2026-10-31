import { fireEvent, render, screen } from "@testing-library/react";
import { expect, test, vi } from "vitest";
import { TrackingProvider } from "../tracking/TrackingContext";
import { PriceCard } from "./PriceCard";

test("clicking a plan reports select_plan with the plan name and price", () => {
  const sink = vi.fn();
  render(
    <TrackingProvider sink={sink}>
      <PriceCard plan="Solo" priceCents={900} />
    </TrackingProvider>,
  );
  fireEvent.click(screen.getByRole("button"));
  expect(sink).toHaveBeenCalledWith({
    component: "PriceCard",
    action: "select_plan",
    label: "Solo",
    value: 900,
  });
});

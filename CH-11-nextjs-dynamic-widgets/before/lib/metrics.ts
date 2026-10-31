export function formatCents(cents: number): string {
  return (cents / 100).toFixed(2);
}

export function retentionRate(startOfMonth: number, lost: number): number {
  return Math.round(((startOfMonth - lost) / startOfMonth) * 100) / 100;
}

export function signupsPerDay(total: number, days: number): number {
  return Math.round(total / days);
}

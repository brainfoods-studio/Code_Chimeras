const INVOICES = [
  { id: 501, customerId: 1, totalCents: 12900 },
  { id: 502, customerId: 2, totalCents: 4400 },
];

function getInvoice(id) {
  return INVOICES.find((invoice) => invoice.id === id) || null;
}

module.exports = { getInvoice };

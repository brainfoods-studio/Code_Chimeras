const BASE = process.env.API_BASE || "http://localhost:3000";

async function fetchJson(pathname) {
  const response = await fetch(BASE + pathname);
  if (!response.ok) {
    throw new Error("GET " + pathname + " failed with status " + response.status);
  }
  return response.json();
}

const getCustomer = (id) => fetchJson("/customers/" + id);
const getInvoice = (id) => fetchJson("/invoices/" + id);
const listProducts = () => fetchJson("/products");

module.exports = { getCustomer, getInvoice, listProducts };

const CUSTOMERS = [
  { id: 1, name: "Harbor Print Co." },
  { id: 2, name: "Linden Bakery" },
];

function listCustomers() {
  return CUSTOMERS;
}

function getCustomer(id) {
  return CUSTOMERS.find((customer) => customer.id === id) || null;
}

module.exports = { listCustomers, getCustomer };

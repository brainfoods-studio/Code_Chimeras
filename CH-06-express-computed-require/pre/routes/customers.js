const express = require("express");
const { listCustomers, getCustomer } = require("../services/customers");

const router = express.Router();

router.get("/", (req, res) => {
  res.json(listCustomers());
});

router.get("/:id", (req, res) => {
  const customer = getCustomer(Number(req.params.id));
  if (!customer) {
    return res.status(404).json({ error: "customer not found" });
  }
  res.json(customer);
});

module.exports = router;

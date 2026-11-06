const express = require("express");
const { getInvoice } = require("../services/invoices");

const router = express.Router();

router.get("/:id", (req, res) => {
  const invoice = getInvoice(Number(req.params.id));
  if (!invoice) {
    return res.status(404).json({ error: "invoice not found" });
  }
  res.json(invoice);
});

module.exports = router;

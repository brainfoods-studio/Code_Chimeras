const express = require("express");
const { listProducts } = require("../services/products");

const router = express.Router();

router.get("/", (req, res) => {
  res.json(listProducts());
});

module.exports = router;

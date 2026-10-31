const express = require("express");

const customersRouter = require("./customers");
const invoicesRouter = require("./invoices");
const productsRouter = require("./products");

const routes = express.Router();

// The one place that lists every URL prefix and the router behind it.
routes.use("/customers", customersRouter);
routes.use("/invoices", invoicesRouter);
routes.use("/products", productsRouter);

module.exports = routes;

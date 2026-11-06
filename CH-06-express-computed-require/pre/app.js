const fs = require("node:fs");
const path = require("node:path");
const express = require("express");

const app = express();
app.use(express.json());

// Every file in routes/ becomes a URL prefix named after the file.
const routesDir = path.join(__dirname, "routes");
for (const file of fs.readdirSync(routesDir)) {
  const name = path.basename(file, ".js");
  app.use("/" + name, require("./routes/" + file));
}

module.exports = app;

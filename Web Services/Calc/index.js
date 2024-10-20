const express = require("express");
const app = express();
const port = 3000;

// Routes for each operation

// Addition
app.get("/add", (req, res) => {
  const { a, b } = req.query;
  const result = parseFloat(a) + parseFloat(b);
  res.send({ operation: "addition", result });
});

// Subtraction
app.get("/subtract", (req, res) => {
  const { a, b } = req.query;
  const result = parseFloat(a) - parseFloat(b);
  res.send({ operation: "subtraction", result });
});

// Multiplication
app.get("/multiply", (req, res) => {
  const { a, b } = req.query;
  const result = parseFloat(a) * parseFloat(b);
  res.send({ operation: "multiplication", result });
});

// Division
app.get("/divide", (req, res) => {
  const { a, b } = req.query;
  if (parseFloat(b) === 0) {
    return res.status(400).send({ error: "Division by zero is not allowed" });
  }
  const result = parseFloat(a) / parseFloat(b);
  res.send({ operation: "division", result });
});

// Start the server
app.listen(port, () => {
  console.log(`Calculator API is running at http://localhost:${port}`);
});

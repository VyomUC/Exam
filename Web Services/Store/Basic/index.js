const express = require("express");
const fs = require("fs");
const app = express();
const port = 3000;

app.use(express.json());

// Read the JSON file
const readItems = () => {
  const data = fs.readFileSync("items.json", "utf8");
  return JSON.parse(data);
};

// Write to the JSON file
const writeItems = (items) => {
  fs.writeFileSync("items.json", JSON.stringify(items, null, 2), "utf8");
};

// GET all items
app.get("/items", (req, res) => {
  const items = readItems();
  res.json(items);
});

// GET a single item by ID
app.get("/items/:id", (req, res) => {
  const items = readItems();
  const item = items.find((i) => i.id === parseInt(req.params.id));
  if (!item) {
    return res.status(404).json({ message: "Item not found" });
  }
  res.json(item);
});

// POST (add) a new item
app.post("/items", (req, res) => {
  const items = readItems();
  const newItem = {
    id: items.length > 0 ? items[items.length - 1].id + 1 : 1,
    name: req.body.name,
    price: req.body.price,
  };
  items.push(newItem);
  writeItems(items);
  res.status(201).json(newItem);
});

// PUT (update) an item by ID
app.put("/items/:id", (req, res) => {
  const id = req.params.id;
  const items = readItems();
  const index = items.findIndex((i) => i.id === parseInt(id));
  if (index === -1) {
    return res.status(404).json({ message: "Item not found" });
  }

  items[index] = {
    id: items[index].id,
    name: req.body.name || items[index].name,
    price: req.body.price || items[index].price,
  };

  writeItems(items);
  res.json(items[index]);
});

// DELETE an item by ID
app.delete("/items/:id", (req, res) => {
  const id = req.params.id;
  let items = readItems();
  const index = items.findIndex((i) => i.id === parseInt(id));
  if (index === -1) {
    return res.status(404).json({ message: "Item not found" });
  }

  items = items.filter((i) => i.id !== parseInt(id));
  writeItems(items);
  res.status(204).send();
});

// Start the server
app.listen(port, () => {
  console.log(`Store API is running at http://localhost:${port}`);
});

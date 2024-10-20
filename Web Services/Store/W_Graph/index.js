const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const fs = require("fs");

const app = express();
const port = 3000;

// Helper functions to interact with items.json
const readItems = () => {
  try {
    const data = fs.readFileSync(path.join(__dirname, "items.json"), "utf8");
    return data ? JSON.parse(data) : []; // Handle empty file
  } catch (error) {
    return [];
  }
};

const writeItems = (items) => {
  fs.writeFileSync("items.json", JSON.stringify(items, null, 2), "utf8");
};

// GraphQL schema
const schema = buildSchema(`
  type Item {
    id: Int
    name: String
    price: Float
  }

  type Query {
    getItem(id: Int!): Item
    getItems: [Item]
  }

  type Mutation {
    addItem(name: String!, price: Float!): Item
    updateItem(id: Int!, name: String, price: Float): Item
    deleteItem(id: Int!): Item
  }
`);

// Resolvers
const root = {
  getItem: ({ id }) => {
    const items = readItems();
    return items.find((item) => item.id === id);
  },
  getItems: () => {
    return readItems();
  },
  addItem: ({ name, price }) => {
    const items = readItems();
    const newItem = {
      id: items.length > 0 ? items[items.length - 1].id + 1 : 1,
      name,
      price,
    };
    items.push(newItem);
    writeItems(items);
    return newItem;
  },
  updateItem: ({ id, name, price }) => {
    const items = readItems();
    const itemIndex = items.findIndex((item) => item.id === id);
    if (itemIndex === -1) {
      throw new Error("Item not found");
    }
    const updatedItem = {
      id,
      name: name || items[itemIndex].name,
      price: price !== undefined ? price : items[itemIndex].price,
    };
    items[itemIndex] = updatedItem;
    writeItems(items);
    return updatedItem;
  },
  deleteItem: ({ id }) => {
    let items = readItems();
    const item = items.find((i) => i.id === id);
    if (!item) {
      throw new Error("Item not found");
    }
    items = items.filter((i) => i.id !== id);
    writeItems(items);
    return item;
  },
};

// Set up GraphQL endpoint
app.use(
  "/graphql",
  graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
  })
);

app.listen(port, () => {
  console.log(
    `Store GraphQL API is running at http://localhost:${port}/graphql`
  );
});

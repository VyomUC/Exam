const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const fs = require("fs");
const path = require("path");
const app = express();
const port = process.env.PORT || 3000;

// Path to the JSON file to store user data
const dataFilePath = path.join(__dirname, "users.json");

// Helper function to read the user data from the JSON file
const readUsersFromFile = () => {
  try {
    const data = fs.readFileSync(dataFilePath, "utf8");
    return JSON.parse(data);
  } catch (error) {
    return []; // Return an empty array if the file doesn't exist or has no data
  }
};

// Helper function to write user data to the JSON file
const writeUsersToFile = (users) => {
  fs.writeFileSync(dataFilePath, JSON.stringify(users, null, 2), "utf8");
};

// Define the GraphQL schema with more user details
const schema = buildSchema(`
  type User {
    name: String!
    email: String!
    age: Int
    address: String
    phone: String
  }

  type Query {
    users: [User]
    user(email: String!): User
  }

  type Mutation {
    createUser(name: String!, email: String!, age: Int, address: String, phone: String): User
    updateUser(email: String!, name: String, newEmail: String, age: Int, address: String, phone: String): User
    deleteUser(email: String!): String
  }
`);

// Define the resolvers
const root = {
  users: () => {
    return readUsersFromFile();
  },
  user: ({ email }) => {
    const users = readUsersFromFile();
    return users.find((user) => user.email === email);
  },
  createUser: ({ name, email, age, address, phone }) => {
    const users = readUsersFromFile();

    if (users.find((user) => user.email === email)) {
      throw new Error("User with this email already exists");
    }

    const newUser = { name, email, age, address, phone };
    users.push(newUser);
    writeUsersToFile(users);
    return newUser;
  },
  updateUser: ({ email, name, newEmail, age, address, phone }) => {
    const users = readUsersFromFile();
    const userIndex = users.findIndex((user) => user.email === email);

    if (userIndex === -1) {
      throw new Error("User not found");
    }

    if (name) users[userIndex].name = name;
    if (newEmail) users[userIndex].email = newEmail;
    if (age !== undefined) users[userIndex].age = age;
    if (address) users[userIndex].address = address;
    if (phone) users[userIndex].phone = phone;

    writeUsersToFile(users);
    return users[userIndex];
  },
  deleteUser: ({ email }) => {
    const users = readUsersFromFile();
    const updatedUsers = users.filter((user) => user.email !== email);

    if (updatedUsers.length === users.length) {
      throw new Error("User not found");
    }

    writeUsersToFile(updatedUsers);
    return `User with email ${email} deleted successfully`;
  },
};

// Set up the GraphQL endpoint
app.use(
  "/graphql",
  graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true, // Enable GraphiQL interface for testing
  })
);

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:3000/graphql`);
});

const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();
const port = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

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

// Route to create a new user (POST /users)
app.post("/users", (req, res) => {
  const user = req.body;
  if (!user.name || !user.email) {
    return res.status(400).json({ error: "Name and email are required" });
  }

  // Read current users from the file
  const users = readUsersFromFile();

  // Check if the user already exists by email
  const existingUser = users.find((u) => u.email === user.email);
  if (existingUser) {
    return res
      .status(400)
      .json({ error: "User with this email already exists" });
  }

  // Add new user to the list
  users.push(user);

  // Write the updated users list back to the file
  writeUsersToFile(users);

  res.status(201).json(user);
});

// Route to get all users (GET /users)
app.get("/users", (req, res) => {
  const users = readUsersFromFile();
  res.json(users);
});

// Route to get a specific user by email (GET /users/:email)
app.get("/users/:email", (req, res) => {
  const email = req.params.email;

  // Read current users from the file
  const users = readUsersFromFile();

  // Find the user by email
  const user = users.find((u) => u.email === email);

  if (!user) {
    return res.status(404).json({ error: "User not found" });
  }

  res.json(user); // Return the specific user
});

// Route to update a user by email (PUT /users/:email)
app.put("/users/:email", (req, res) => {
  const email = req.params.email;
  const updatedUser = req.body;

  if (!updatedUser.name || !updatedUser.email) {
    return res.status(400).json({ error: "Name and email are required" });
  }

  // Read current users from the file
  const users = readUsersFromFile();

  // Find the user by email
  const userIndex = users.findIndex((u) => u.email === email);

  if (userIndex === -1) {
    return res.status(404).json({ error: "User not found" });
  }

  // Update the user details
  users[userIndex] = { ...users[userIndex], ...updatedUser };

  // Write the updated users list back to the file
  writeUsersToFile(users);

  res.json(users[userIndex]); // Return the updated user
});

// Route to delete a user by email (DELETE /users/:email)
app.delete("/users/:email", (req, res) => {
  const email = req.params.email;

  // Read current users from the file
  const users = readUsersFromFile();

  // Filter out the user to delete
  const updatedUsers = users.filter((u) => u.email !== email);

  if (updatedUsers.length === users.length) {
    return res.status(404).json({ error: "User not found" });
  }

  // Write the updated users list back to the file
  writeUsersToFile(updatedUsers);

  res.status(204).send(); // No content to return
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

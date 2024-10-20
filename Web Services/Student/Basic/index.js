const express = require("express");
const fs = require("fs");
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Path to the JSON file
const dataFilePath = "students.json";

// Helper function to read data from JSON file
const readDataFromFile = () => {
  const data = fs.readFileSync(dataFilePath, "utf8");
  return JSON.parse(data);
};

// Helper function to write data to JSON file
const writeDataToFile = (data) => {
  fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2), "utf8");
};

// Get all students
app.get("/students", (req, res) => {
  const data = readDataFromFile();
  res.json(data.students);
});

// Get a single student by ID
app.get("/students/:id", (req, res) => {
  const data = readDataFromFile();
  const student = data.students.find((student) => student.id === req.params.id);
  if (student) {
    res.json(student);
  } else {
    res.status(404).send("Student not found");
  }
});

// Add a new student
app.post("/students", (req, res) => {
  const { name, age, courses: courseIds } = req.body;
  const data = readDataFromFile();

  const newStudent = {
    id: `${data.students.length + 1}`,
    name,
    age,
    courses: courseIds.map((id) =>
      data.courses.find((course) => course.id === id)
    ),
  };

  data.students.push(newStudent);
  writeDataToFile(data);

  res.status(201).json(newStudent);
});

// Update a student by ID
app.put("/students/:id", (req, res) => {
  const { name, age, courses: courseIds } = req.body;
  const data = readDataFromFile();
  const student = data.students.find((student) => student.id === req.params.id);

  if (!student) {
    return res.status(404).send("Student not found");
  }

  if (name !== undefined) student.name = name;
  if (age !== undefined) student.age = age;
  if (courseIds !== undefined)
    student.courses = courseIds.map((id) =>
      data.courses.find((course) => course.id === id)
    );

  writeDataToFile(data);

  res.json(student);
});

// Delete a student by ID
app.delete("/students/:id", (req, res) => {
  const data = readDataFromFile();
  const studentIndex = data.students.findIndex(
    (student) => student.id === req.params.id
  );

  if (studentIndex === -1) {
    return res.status(404).send("Student not found");
  }

  data.students.splice(studentIndex, 1);
  writeDataToFile(data);

  res.send(`Student with ID ${req.params.id} was deleted`);
});

// Get all courses
app.get("/courses", (req, res) => {
  const data = readDataFromFile();
  res.json(data.courses);
});

// Get a single course by ID
app.get("/courses/:id", (req, res) => {
  const data = readDataFromFile();
  const course = data.courses.find((course) => course.id === req.params.id);
  if (course) {
    res.json(course);
  } else {
    res.status(404).send("Course not found");
  }
});

// Add a new course
app.post("/courses", (req, res) => {
  const { title, description } = req.body;
  const data = readDataFromFile();

  const newCourse = {
    id: `${data.courses.length + 1}`,
    title,
    description,
  };

  data.courses.push(newCourse);
  writeDataToFile(data);

  res.status(201).json(newCourse);
});

// Start the server
app.listen(4000, () => {
  console.log("Server is running on http://localhost:4000");
});

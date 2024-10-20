const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const fs = require("fs");

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

// GraphQL schema
const schema = buildSchema(`
  type Student {
    id: ID!
    name: String!
    age: Int!
    courses: [Course]
  }

  type Course {
    id: ID!
    title: String!
    description: String!
  }

  type Query {
    getStudent(id: ID!): Student
    getAllStudents: [Student]
    getCourse(id: ID!): Course
    getAllCourses: [Course]
  }

  type Mutation {
    addStudent(name: String!, age: Int!, courses: [ID]!): Student
    updateStudent(id: ID!, name: String, age: Int, courses: [ID]): Student
    deleteStudent(id: ID!): String
    addCourse(title: String!, description: String!): Course
  }
`);

// Helper functions to interact with data
const getStudentById = (id) => {
  const { students } = readDataFromFile();
  return students.find((student) => student.id === id);
};

const getCourseById = (id) => {
  const { courses } = readDataFromFile();
  return courses.find((course) => course.id === id);
};

const root = {
  getStudent: ({ id }) => getStudentById(id),
  getAllStudents: () => {
    const { students } = readDataFromFile();
    return students;
  },
  getCourse: ({ id }) => getCourseById(id),
  getAllCourses: () => {
    const { courses } = readDataFromFile();
    return courses;
  },

  addStudent: ({ name, age, courses: courseIds }) => {
    const data = readDataFromFile();
    const newStudent = {
      id: `${data.students.length + 1}`,
      name,
      age,
      courses: courseIds.map((id) => getCourseById(id)),
    };
    data.students.push(newStudent);
    writeDataToFile(data);
    return newStudent;
  },

  updateStudent: ({ id, name, age, courses: courseIds }) => {
    const data = readDataFromFile();
    const student = data.students.find((student) => student.id === id);
    if (!student) {
      throw new Error("Student not found");
    }
    if (name !== undefined) student.name = name;
    if (age !== undefined) student.age = age;
    if (courseIds !== undefined)
      student.courses = courseIds.map((id) => getCourseById(id));

    writeDataToFile(data);
    return student;
  },

  deleteStudent: ({ id }) => {
    const data = readDataFromFile();
    const index = data.students.findIndex((student) => student.id === id);
    if (index === -1) {
      throw new Error("Student not found");
    }
    data.students.splice(index, 1);
    writeDataToFile(data);
    return `Student with ID ${id} was deleted`;
  },

  addCourse: ({ title, description }) => {
    const data = readDataFromFile();
    const newCourse = {
      id: `${data.courses.length + 1}`,
      title,
      description,
    };
    data.courses.push(newCourse);
    writeDataToFile(data);
    return newCourse;
  },
};

// Create an Express app
const app = express();

// Define the GraphQL endpoint
app.use(
  "/graphql",
  graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true, // Enable GraphiQL interface
  })
);

// Start the server
app.listen(4000, () => {
  console.log("Server is running on http://localhost:4000/graphql");
});

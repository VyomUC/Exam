To add a course:

    mutation {
        addCourse(title: "Math 101", description: "Basic Mathematics") {
            id
            title
            description
        }
    }


To add a student:

    mutation {
        addStudent(name: "John Doe", age: 20, courses: ["1"]) {
            id
            name
            age
            courses {
            title
            description
            }
        }
    }


To fetch all students:

    query {
        getAllStudents {
            id
            name
            age
            courses {
            title
            }
        }
    }


To fetch a specific student by ID:

    query {
        getStudent(id: "1") {
            name
            age
            courses {
            title
            }
        }
    }


To update a student:

    mutation {
        updateStudent(id: "1", name: "John Smith", age: 21) {
            id
            name
            age
        }
    }


To delete a student:

mutation {
  deleteStudent(id: "1")
}
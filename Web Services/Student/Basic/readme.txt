GET /students

    Request: GET http://localhost:4000/students


GET /students/:id

    Request: GET http://localhost:4000/students/1 (replace 1 with the student's ID)


POST http://localhost:4000/students

    {
        "name": "Jane Doe",
        "age": 22,
        "courses": ["1"]
    }


PUT /students/:id

    PUT http://localhost:4000/students/1

    {
        "name": "John Smith",
        "age": 23,
        "courses": ["2"]
    }


DELETE /students/:id

    Request: DELETE http://localhost:4000/students/1


GET http://localhost:4000/courses


GET /courses/:id

    Request: GET http://localhost:4000/courses/1


POST /courses

    POST http://localhost:4000/courses

    {
        "title": "Physics 101",
        "description": "Introduction to Physics"
    }
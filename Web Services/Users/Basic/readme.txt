Create a New User
    Method: POST
    URL: http://localhost:3000/users

    {
    "name": "John Doe",
    "email": "john.doe@example.com"
    }


Get All Users (GET /users)
    Method: GET
    URL: http://localhost:3000/users


Get a Specific User (GET /users/)
    Method: GET
    URL: http://localhost:3000/users/@example.com


Update a User (PUT /users/)
    Method: PUT
    URL: http://localhost:3000/users/@example.com

    {
    "name": "John Doe Updated",
    "email": "john.doe@example.com"
    }


Delete a User (DELETE /users/)
    Method: DELETE
    URL: http://localhost:3000/users/@example.com
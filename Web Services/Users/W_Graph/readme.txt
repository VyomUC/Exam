http://localhost:3000/graphql

Create a New User (Mutation):

    mutation {
        createUser(
            name: "Jane Doe",
            email: "jane.doe@example.com",
            age: 30,
            address: "123 Main St, Anytown, USA",
            phone: "123-456-7890"
        ) {
            name
            email
            age
            address
            phone
        }
    }


Get All Users (Query):

    query {
        users {
            name
            email
            age
            address
            phone
        }
    }


Get a Specific User by Email (Query):

    query {
        user(email: "jane.doe@example.com") {
            name
            email
            age
            address
            phone
        }
    }


Update a User (Mutation):

    mutation {
        updateUser(
            email: "jane.doe@example.com",
            name: "Jane Updated",
            age: 31,
            address: "456 New Ave, Newtown, USA",
            phone: "987-654-3210"
        ) {
            name
            email
            age
            address
            phone
        }
    }


E. Delete a User by Email (Mutation):

    mutation {
    deleteUser(email: "jane.doe@example.com")
    }
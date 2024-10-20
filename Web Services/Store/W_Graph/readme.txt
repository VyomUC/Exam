Get all items (Query)

    {
        getItems {
            id
            name
            price
        }
    }


Get an item by ID (Query)

    {
        getItem(id: 1) {
            id
            name
            price
        }
    }


Add a new item (Mutation)

    mutation {
    addItem(name: "Orange", price: 0.75) {
        id
        name
        price
    }
    }


Update an item (Mutation)

    mutation {
        updateItem(id: 1, name: "Green Apple", price: 0.6) {
            id
            name
            price
        }
    }


Delete an item (Mutation)

    mutation {
        deleteItem(id: 1) {
            id
            name
            price
        }
    }
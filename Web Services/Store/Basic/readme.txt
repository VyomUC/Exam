GET /items – Get all items
    Method: GET
    URL: http://localhost:3000/items


GET /items/
    Method: GET
    URL: http://localhost:3000/items/1


POST /items – Add a new item
    Method: POST
    URL: http://localhost:3000/items

    {
        "name": "Orange",
        "price": 0.75
    }


PUT /items/
    Method: PUT
    URL: http://localhost:3000/items/1

    {
        "name": "Green Apple",
        "price": 0.6
    }


DELETE /items/
Method: DELETE
    URL: http://localhost:3000/items/1
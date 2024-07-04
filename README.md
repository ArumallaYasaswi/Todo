# Todo
Create a DRF application that manages a simple todo list. The API should allow users to perform CRUD (Create, Read, Update, Delete) operations on the todo items.


# http end points

Endpoint: POST /todos/
Request Body: JSON object containing title (string) and description (string, optional)
Response: JSON object with the created todo item including a unique id, title, description, and
completed status (default to False)

1.) id field is auto assigned (readonly) cannot assgin value
actual input:

Media type:
           application/json
Content:
{
        "id": 22,
        "title": "d",
        "description": "dsdffDFDFF",
        "completed": true
    }


actual output:
Todolistcreate
DESC: used to LIST, CREATE a todo item.
POST /todos/
HTTP 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": "'ID field cannot be provided'"
    }
]

2.) description is optinal
actual input:
{
        "title": "d",
        "completed": true
    }
actual output:

HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": "d",
    "description": null,
    "completed": true,
    "id": 10
}

----------------------------------------------------------------------------------------------------------------------------------
Read All Todo Items
===================
Endpoint: GET /todos/
Response: JSON array of all todo items

actual input: GET /todos/
actual response:
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "sdd",
        "description": "dsdffDFDFF",
        "completed": true
    },
    {
        "id": 2,
        "title": "d",
        "description": "dsdffDFDFF",
        "completed": true
    },
    {
        "id": 3,
        "title": "sdd",
        "description": "dsdffDFDFF",
        "completed": true
    },
    {
        "id": 4,
        "title": "sdd",
        "description": "dsdffDFDFF",
        "completed": true
    },
    
]


----------------------------------------------------------------------------------------------------------------------------------
Read a Single Todo Item
=======================
Endpoint: GET /todos/{todo_id}
Path Parameter: todo_id (integer)
Response: JSON object of the requested todo item
1.) id matches
actual input:
GET /todos/1/

actual output:
HTTP 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "title": "sdsdd",
    "description": "Df",
    "completed": true
}

2.)
actual input:
GET /todos/1/

actaul output:
HTTP 404 Not Found
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Todo not found"
}
----------------------------------------------------------------------------------------------------------------------------------

Update a Todo Item
==================
Endpoint: PUT /todos/{todo_id}
Path Parameter: todo_id (integer)
Request Body: JSON object containing title (string), description (string, optional), and completed
(boolean)
Response: JSON object with the updated todo item

actual input:
PUT /todos/2/
1.)notifies the error msg 
{
    "id": 2,
    "title": "sdd",
    "description": null,
    "completed": true
}
actual output:
HTTP 400 Bad Request
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": "'ID field cannot be updated.'"
    }
]

2.)put option with pout errors

actual input: put request
Content-Type: application/json

{
    "title": "moring routinue",
    "description": null,
    "completed": true
}
actual output:
PUT /todos/2/
HTTP 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "title": "moring routinue",
    "description": null,
    "completed": true
}


----------------------------------------------------------------------------------------------------------------------------------
Delete a Todo Item
==================
Endpoint: DELETE /todos/{todo_id}
Path Parameter: todo_id (integer)
Response: JSON object confirming deletion of the todo item

actaul input
DELETE /todos/1/

actual output: 
HTTP 204 No Content
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Requirments


Use Python and FastAPI to implement the API.


Use Pydantic for data validation and serialization.
->used manual vaidation, and serilizer validation for fields

Store the todo items in an in-memory list (no database required).
->used persistent storage to store detils of all todo lists in "./todos.json" file

Handle error cases such as invalid todo IDs gracefully, returning appropriate HTTP status codes
and error messages.

Write clear and concise code with comments explaining the logic.
Provide a README.md file with instructions on how to run the application locally.


USER_CREATE = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string"
        },
        "email": {
            "type": "string",
        },

        "password": {
            "type": "string",
            "pattern": "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        }
    },
    "required": ["username", "email", "password"]
}

POST_CREATE = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "content": {
            "type": "string",
        },
    },
    "required": ["title", "content"]
}
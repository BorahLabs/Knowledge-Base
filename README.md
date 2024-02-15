# Knowledge Database

## Requirements

- Docker
- Docker Compose

## How to run

- Clone this repository
- Create an `.env` file. You can copy the contents of `.env.example` and make any necessary changes
- Run `docker-compose build` to build the image
- Run `docker-compose up -d` to run the containers

## Endpoints

### `POST` `/insert`

Insert new knowledge into the database. The body must be a JSON with the following structure:

```json
{
    "data": [
        {
            "id": "08c8ded7-49cc-4746-b2eb-6330c811b7a9",
            "text": "Text that will be converted to embeddings",
            "entity": "Name of the entity that will be used to filter if needed",
            "payload": {
                "key": "optional"
            }
        }
    ]
}
```

### `GET` `/query`

This endpoint can receive the following parameters:

- `query`: Query to search for
- `k`: Number of results to return. Default = 5
- `entities`: Comma separated list of entities to filter the results. Default = all entities

### `DELETE` `/delete/{id}`

Delete a knowledge from the database. The `id` parameter is the id of the knowledge to delete.

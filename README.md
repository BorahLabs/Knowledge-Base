# Knowledge Database

## Requirements

- Docker

## How to run

- Clone this repository
- Create an `.env` file. You can copy the contents of `.env.example` and make any necessary changes
- Run `docker build -t knowledge-database .` to build the image
- Run `docker run -p 8000:8000 -d knowledge-database` to run the container

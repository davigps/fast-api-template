# FastAPI - Backend Template

FastAPI Backend template, with:

- AWS S3 integration
- Image Upload
- JWT Authentication
- Alembic for migrations
- Pydantic for models
- Tests with Pytest

#### Models

- User
- Post
- PostCategory

## Pre-requisites

- Poetry (https://python-poetry.org/docs/#installation)
- Docker (https://www.docker.com/get-started/)
  - Docker Compose (https://docs.docker.com/compose/install/)
- Make (https://www.gnu.org/software/make/)

## Installation

- Clone the repository
- Set poetry environment in folder `poetry config virtualenvs.in-project true`
- Run `make install` to install dependencies
- Run `make db-up` to start the database
- Run `make start` to run server for the first time and run migrations
- (Optionally) Run `make db-seed` to run seed and fill database with fake data

## Run

- Run `make start` to run server
- Access (http://localhost:8000/docs) to see the documentation
- To run tests run `make test`

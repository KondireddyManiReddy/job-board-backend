# Job Board API

A REST API backend application built using FastAPI and PostgreSQL.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Swagger UI

## Features

- User Registration
- User Login with JWT Authentication
- Create Jobs
- View Jobs
- Update Jobs
- Delete Jobs
- Apply for Jobs
- View Applications

## API Endpoints

### Users

POST /users/register

POST /users/login


### Jobs

GET /jobs/

POST /jobs/

GET /jobs/{job_id}

PUT /jobs/{job_id}

DELETE /jobs/{job_id}


### Applications

POST /applications/

GET /applications/

## Run Project

Install dependencies:

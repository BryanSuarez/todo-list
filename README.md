# Todo App with FastAPI and Docker

This is a simple Todo list application built with FastAPI, using MySQL as the database, and containerized with Docker.
The project is organized following a modular structure.

## Prerequisites

*   Docker
*   Docker Compose

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <directory-name>
    ```

2.  **Create Environment File:**
    Copy the example environment file and fill in your database credentials:
    ```bash
    cp .env.example .env
    ```
    Edit the `.env` file with your actual database user, password, name, and desired host port mapping. Ensure the `MYSQL_ROOT_PASSWORD` is set securely.

## Running the Application with Docker Compose

1.  **Build and Run Containers:**
    From the project root directory (where `docker-compose.yml` is located), run:
    ```bash
    docker compose up --build -d
    ```
    *   `--build`: Builds the FastAPI application image if it doesn't exist or if the `Dockerfile` changed.
    *   `-d`: Runs the containers in detached mode (in the background).

2.  **Accessing the Application:**
    *   **API:** The FastAPI application will be available at `http://127.0.0.1:8001` (Port 8001 on the host maps to 8000 in the container by default in `docker-compose.yml`).
    *   **Database:** The MySQL database will be accessible from your host machine on the port specified by `DB_PORT` in your `.env` file (e.g., `127.0.0.1:3310` if `DB_PORT=3310`).

3.  **Stopping the Application:**
    To stop the running containers:
    ```bash
    docker compose down
    ```
    Use `docker compose down -v` if you also want to remove the database volume (all data will be lost).

## API Documentation

Once the application is running, FastAPI automatically generates interactive API documentation.

*   **Swagger UI:** `http://127.0.0.1:8001/docs`
*   **ReDoc:** `http://127.0.0.1:8001/redoc`

## Project Structure

```
├── app/
│   ├── __init__.py         # Makes 'app' a Python package
│   ├── main.py             # FastAPI application entry point, DB init
│   ├── database.py         # SQLAlchemy setup (engine, session, Base)
│   ├── api/                # API modules (routers)
│   │   ├── __init__.py
│   │   └── categories.py   # Endpoints for categories
│   ├── models/             # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── category.py     # Category table model
│   ├── schemas/            # Pydantic models (data validation)
│   │   ├── __init__.py
│   │   └── category.py     # Schemas for categories
│   └── services/           # Business logic
│       ├── __init__.py
│       └── category_service.py # Logic for categories CRUD with DB
├── .env                    # Environment variables (DB credentials) - *ignored by git*
├── .env.example            # Example environment variables file
├── .gitignore              # Specifies intentionally untracked files that Git should ignore
├── Dockerfile              # Instructions to build the FastAPI app Docker image
├── docker-compose.yml      # Defines Docker services (web app, database)
└── requirements.txt        # Python dependencies
``` 
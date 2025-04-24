# Todo App with FastAPI

This is a simple Todo list application built with FastAPI and organized following a modular project structure.

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd <directory-name>
    ```

2.  **Create a virtual environment:**
    It's recommended to use `uv` to manage the virtual environment and dependencies.
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows (cmd.exe):
        ```bash
        .venv\Scripts\activate.bat
        ```
    *   On Windows (PowerShell):
        ```bash
        .venv\Scripts\Activate.ps1
        ```

4.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

## Running the Application

To start the development server (with auto-reload):

```bash
uvicorn app.main:app --reload --port 8001
```

The API will be available at `http://127.0.0.1:8001`.

## API Documentation

FastAPI automatically generates interactive API documentation.

*   **Swagger UI:** `http://127.0.0.1:8001/docs`
*   **ReDoc:** `http://127.0.0.1:8001/redoc`

## Project Structure

```
├── app/
│   ├── __init__.py       # Makes 'app' a Python package
│   ├── main.py           # FastAPI application entry point
│   ├── api/              # API modules (routers)
│   │   ├── __init__.py
│   │   └── categories.py # Endpoints for categories
│   ├── schemas/          # Pydantic models (data validation)
│   │   ├── __init__.py
│   │   └── category.py   # Schemas for categories
│   └── services/         # Business logic
│       ├── __init__.py
│       └── category_service.py # Logic for categories
├── .venv/                # Virtual environment (managed by uv)
├── requirements.txt      # Project dependencies
└── README.md             # This file
``` 
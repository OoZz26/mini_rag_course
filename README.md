# MINI_RAG API

This is a FastAPI-based backend application for the MINI_RAG project. It provides endpoints for basic application metadata and file uploading functionalities per project.

## Directory Structure

- `src/main.py`: The entry point of the FastAPI application.
- `src/Routes/`: Contains API route definitions (`base.py`, `data.py`).
- `src/controllers/`: Contains business logic for handling data and projects (`DataController.py`, `ProjectController.py`, `BaseController.py`).
- `src/models/`: Contains data models and enums (e.g., `ResponseStatus`).
- `src/helpers/`: Contains helper scripts, like `config.py` for environment variables using Pydantic Settings.

## Setup & Installation

1. Clone the repository or navigate to the project directory:
   ```bash
   cd mini_rag_course
   ```

2. Create a virtual environment (optional but recommended) and install the dependencies:
   ```bash
   pip install -r src/rquirements.txt
   ```
   *Note: Requirements include `fastapi`, `uvicorn`, `python-multipart`, `python-dotenv`, `pydantic-settings`, and `aiofiles`.*

3. Set up the environment variables. Copy `.env.example` to `.env` and configure accordingly:
   ```env
   App_Name=MINI_RAG
   App_Version=1.0.0
   SECRET_KEY=your_secret_key
   FILE_ALLOWED_EXTENSIONS=["application/pdf", "text/plain"]
   MAX_FILE_SIZE_MB=10
   FILE_DEFAULT_CHUNK_SIZE=1048576
   ```

## Running the Application

To run the application, use Uvicorn:

```bash
cd src
uvicorn main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Base Router
- **GET `/base/`**: Returns a welcome message along with the `app_name` and `app_version` configured in the `.env` file.

### Data Router
- **POST `/data/upload/{project_id}`**: Uploads a file for a given `project_id`. The file's extension and size are validated against the environment settings. Files are saved async in chunks to prevent memory overload.

## License
MIT
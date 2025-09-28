# Backend Development Guide

## Table of Contents

1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Route Architecture](#route-architecture)
4. [Exception Handling](#exception-handling)
5. [Adding New Features](#adding-new-features)
6. [Adding External Services](#adding-external-services)
7. [Development Guidelines](#development-guidelines)
8. [Testing Strategy](#testing-strategy)

## Project Overview

This is a FastAPI-based backend application following a feature-driven architecture with clear separation of concerns.
The project uses:

- **FastAPI** for the web framework
- **Pydantic** for data validation and serialization
- **UV** for dependency management
- **Ruff** for linting and formatting
- **Pre-commit** hooks for code quality
- **Docker** for containerization

## Folder Structure

```
src/
├── __main__.py                 # Application entry point
└── backend/
    ├── __init__.py
    ├── api/                    # API layer configuration
    │   ├── __init__.py
    │   ├── _granian.py         # Granian server configuration
    │   ├── application.py      # FastAPI app factory
    │   ├── cli.py             # CLI commands
    │   └── lifespan.py        # App lifecycle management
    ├── core/                   # Core application components
    │   ├── __init__.py
    │   ├── config/            # Configuration management
    │   │   ├── __init__.py
    │   │   └── base.py        # Base configuration classes
    │   ├── connection/        # Database/external connections
    │   │   └── __init__.py
    │   ├── constants/         # Application constants
    │   │   ├── __init__.py
    │   │   └── status.py      # HTTP status constants
    │   ├── middlewares/       # Custom middlewares
    │   │   ├── __init__.py
    │   │   └── logger.py      # Logging middleware
    │   └── utils/            # Utility functions
    │       ├── __init__.py
    │       ├── helper.py      # General helper functions
    │       └── logging.py     # Logging utilities
    ├── database/              # Data access layer
    │   ├── __init__.py
    │   ├── base_dao.py        # Base Data Access Object
    │   └── file_dao.py        # File-specific DAO
    ├── errors/                # Custom exception classes
    │   └── __init__.py
    ├── features/              # Feature modules (business logic)
    │   ├── __init__.py
    │   ├── llama/            # LLaMA integration feature
    │   │   └── __init__.py
    │   └── storage/          # File storage feature
    │       ├── __init__.py
    │       ├── controller.py  # Business logic controller
    │       ├── models.py      # Database models
    │       ├── routes.py      # API routes
    │       └── schemas.py     # Request/Response schemas
    ├── schema/               # Global schemas
    │   ├── __init__.py
    │   ├── base.py           # Base schema classes
    │   └── response.py       # Response schemas
    └── services/             # External service integrations
        ├── __init__.py
        ├── s3_service.py     # AWS S3 integration
        └── repositories/     # Repository pattern implementations
            ├── __init__.py
            └── storage_repository.py
```

### Key Directory Explanations

#### `/api/`

Contains FastAPI application setup, server configuration, and lifecycle management.

#### `/core/`

Houses core application components including configuration, middlewares, utilities, and constants.

#### `/features/`

Each subdirectory represents a business domain/feature with its own:

- **routes.py**: API endpoints
- **controller.py**: Business logic
- **schemas.py**: Request/Response models
- **models.py**: Database models

#### `/services/`

External service integrations and repository pattern implementations.

#### `/database/`

Data Access Objects (DAOs) for database operations.

## Route Architecture

### Route Organization

Routes are organized by feature in a factory pattern:

```python
from fastapi import APIRouter, UploadFile, status

from backend.features.storage.schemas import (
	FileUploadResponse,
)
from src.backend.features.storage.controller import StorageController


# features/storage/routes.py
def create_storage_router() -> APIRouter:
	"""Create and configure the storage router."""
	router = APIRouter(prefix="/storage", tags=["storage"])
	controller = StorageController()

	@router.post("/upload", status_code=status.HTTP_201_CREATED)
	async def upload_file(file: UploadFile) -> FileUploadResponse:
		return await controller.upload_file(file)

	return router
```

### Route Registration

Routes are registered in the main application through feature modules:

```python
# api/application.py
from backend.features import api

app.include_router(api.router, prefix="/api")
```

### Route Patterns

1. **RESTful Design**: Follow REST conventions
	- `GET /api/storage/files` - List resources
	- `POST /api/storage/upload` - Create resource
	- `GET /api/storage/files/{id}` - Get specific resource
	- `PUT /api/storage/files/{id}` - Update resource
	- `DELETE /api/storage/files/{id}` - Delete resource

2. **Consistent Response Format**: All endpoints return structured responses
3. **Proper Status Codes**: Use appropriate HTTP status codes
4. **Documentation**: Include summary and description for OpenAPI

## Exception Handling

### Custom Exception Classes

Create custom exceptions in the `/errors/` directory:

```python
# errors/storage_errors.py
from fastapi import HTTPException, status


class FileNotFoundError(HTTPException):
	def __init__(self, file_id: int):
		super().__init__(
				status_code=status.HTTP_404_NOT_FOUND,
				detail=f"File with id {file_id} not found"
		)


class FileSizeTooLargeError(HTTPException):
	def __init__(self, max_size: int):
		super().__init__(
				status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
				detail=f"File size exceeds maximum allowed size of {max_size} bytes"
		)
```

### Exception Handling in Controllers

```python
# features/storage/controller.py
async def get_file_info(self, file_id: int) -> FileInfoResponse:
	try:
		file_data = await self.service.get_file_by_id(file_id)
		if not file_data:
			raise FileNotFoundError(file_id)
		return FileInfoResponse(**file_data)
	except DatabaseError as e:
		logger.error(f"Database error: {e}")
		raise HTTPException(
				status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
				detail="Internal server error"
		)
```

### Global Exception Handlers

Register global exception handlers in the application factory:

```python
# api/application.py
@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
	return JSONResponse(
			status_code=exc.status_code,
			content={"detail": exc.detail, "type": "custom_error"}
	)
```

## Adding New Features

### Step-by-Step Guide

1. **Create Feature Directory**
   ```bash
   mkdir src/backend/features/new_feature
   touch src/backend/features/new_feature/__init__.py.jinja
   ```

2. **Create Core Files**
   ```bash
   # Create the essential files
   touch src/backend/features/new_feature/routes.py
   touch src/backend/features/new_feature/controller.py
   touch src/backend/features/new_feature/schemas.py
   touch src/backend/features/new_feature/models.py
   ```

3. **Define Schemas** (`schemas.py`)
   ```python
   from backend.schema.base import BaseSchema

   class CreateItemRequest(BaseSchema):
       name: str
       description: str | None = None

   class ItemResponse(BaseSchema):
       id: int
       name: str
       description: str | None
       created_at: datetime
   ```

4. **Create Database Models** (`models.py`)
   ```python
   from sqlalchemy import Column, Integer, String, DateTime
   from backend.database.base import Base

   class Item(Base):
       __tablename__ = "items"

       id = Column(Integer, primary_key=True)
       name = Column(String, nullable=False)
       description = Column(String, nullable=True)
       created_at = Column(DateTime, default=datetime.utcnow)
   ```

5. **Implement Controller** (`controller.py`)
   ```python
   from backend.features.new_feature.schemas import CreateItemRequest, ItemResponse

   class NewFeatureController:
       def __init__(self):
           self.repository = NewFeatureRepository()

       async def create_item(self, request: CreateItemRequest) -> ItemResponse:
           # Business logic here
           pass
   ```

6. **Define Routes** (`routes.py`)
   ```python
   from fastapi import APIRouter, status
   from .controller import NewFeatureController
   from .schemas import CreateItemRequest, ItemResponse

   def create_new_feature_router() -> APIRouter:
       router = APIRouter(prefix="/new-feature", tags=["new-feature"])
       controller = NewFeatureController()

       @router.post("/items", status_code=status.HTTP_201_CREATED)
       async def create_item(request: CreateItemRequest) -> ItemResponse:
           return await controller.create_item(request)

       return router
   ```

7. **Register Routes**
   Update `features/__init__.py` to include your new router:
   ```python
   from fastapi import APIRouter
   from .storage.routes import create_storage_router
   from .new_feature.routes import create_new_feature_router

   api_router = APIRouter()
   api_router.include_router(create_storage_router())
   api_router.include_router(create_new_feature_router())
   ```

8. **Add Tests**
   ```bash
   mkdir tests/features/new_feature
   touch tests/features/new_feature/test_routes.py
   touch tests/features/new_feature/test_controller.py
   ```

## Adding External Services

### Step-by-Step Guide

1. **Create Service Class**
   ```bash
   touch src/backend/services/new_service.py
   ```

2. **Implement Service** (`services/new_service.py`)
   ```python
   import httpx
   from typing import Optional
   from backend.core.config import settings

   class NewExternalService:
       def __init__(self):
           self.base_url = settings.new_service.base_url
           self.api_key = settings.new_service.api_key
           self.client = httpx.AsyncClient()

       async def make_request(self, endpoint: str, data: dict) -> dict:
           try:
               response = await self.client.post(
                   f"{self.base_url}/{endpoint}",
                   json=data,
                   headers={"Authorization": f"Bearer {self.api_key}"}
               )
               response.raise_for_status()
               return response.json()
           except httpx.HTTPError as e:
               logger.error(f"External service error: {e}")
               raise ExternalServiceError(str(e))

       async def close(self):
           await self.client.aclose()
   ```

3. **Add Configuration**
   Update `core/config/base.py`:
   ```python
   class NewServiceConfig(BaseSettings):
       base_url: str
       api_key: str
       timeout: int = 30

       class Config:
           env_prefix = "NEW_SERVICE_"

   class Settings(BaseSettings):
       new_service: NewServiceConfig = NewServiceConfig()
   ```

4. **Create Repository** (`services/repositories/new_service_repository.py`)
   ```python
   from backend.services.new_service import NewExternalService

   class NewServiceRepository:
       def __init__(self):
           self.service = NewExternalService()

       async def process_data(self, data: dict) -> dict:
           return await self.service.make_request("process", data)
   ```

5. **Add Environment Variables**
   Update `.env`:
   ```
   NEW_SERVICE_BASE_URL=https://api.newservice.com
   NEW_SERVICE_API_KEY=your_api_key_here
   NEW_SERVICE_TIMEOUT=30
   ```

6. **Add Service Management to Lifespan**
   Update `api/lifespan.py`:
   ```python
   @asynccontextmanager
   async def lifespan(app: FastAPI):
       # Startup
       new_service = NewExternalService()
       app.state.new_service = new_service

       yield

       # Shutdown
       await new_service.close()
   ```

## Development Guidelines

### Code Quality Standards

1. **Type Hints**: All functions must have proper type hints
2. **Docstrings**: Use Google-style docstrings for classes and functions
3. **Error Handling**: Implement proper exception handling
4. **Logging**: Use structured logging with appropriate levels

### Naming Conventions

- **Files**: Use snake_case (e.g., `user_service.py`)
- **Classes**: Use PascalCase (e.g., `UserService`)
- **Functions/Variables**: Use snake_case (e.g., `get_user_data`)
- **Constants**: Use UPPER_SNAKE_CASE (e.g., `MAX_FILE_SIZE`)

### Git Workflow

1. **Branch Naming**:
	- Features: `feature/feature-name`
	- Bug fixes: `fix/bug-description`
	- Hotfixes: `hotfix/critical-issue`

2. **Commit Messages**: Use conventional commits format
   ```
   feat: add user authentication endpoint
   fix: resolve file upload validation issue
   docs: update API documentation
   ```

3. **Pre-commit Hooks**: Ensure all hooks pass before committing
   ```bash
   task pre-commit
   ```

### Development Workflow

1. **Setup Development Environment**
   ```bash
   task setup  # Bootstrap the entire project
   ```

2. **Run Development Server**
   ```bash
   task run    # Start the application
   ```

3. **Run Tests**
   ```bash
   task test   # Full test suite with coverage
   task test-u # Unit tests only
   ```

4. **Code Quality Checks**
   ```bash
   task lint   # Run linters and formatters
   ```

## Testing Strategy

### Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Test configuration and fixtures
├── unit/                    # Unit tests
│   ├── features/
│   │   └── storage/
│   │       ├── test_controller.py
│   │       └── test_schemas.py
│   └── services/
│       └── test_s3_service.py
└── integration/            # Integration tests
    ├── test_storage_api.py
    └── test_database.py
```

### Test Categories

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **API Tests**: Test HTTP endpoints end-to-end

### Writing Tests

```python
# tests/unit/features/storage/test_controller.py
import pytest
from backend.features.storage.controller import StorageController
from unittest.mock import AsyncMock, MagicMock


@pytest.fixture
def storage_controller():
	controller = StorageController()
	controller.repository = AsyncMock()
	return controller


@pytest.mark.asyncio
async def test_get_file_info_success(storage_controller):
	# Arrange
	file_id = 1
	expected_data = {"id": 1, "filename": "test.txt"}
	storage_controller.service.get_file_by_id.return_value = expected_data

	# Act
	result = await storage_controller.get_file_info(file_id)

	# Assert
	assert result.id == 1
	assert result.filename == "test.txt"
	storage_controller.service.get_file_by_id.assert_called_once_with(file_id)
```

---

## Quick Reference Commands

```bash
# Project setup
task setup              # Complete project bootstrap

# Development
task run               # Start development server
task docker           # Run in Docker container

# Code quality
task lint             # Run all linters and formatters
task pre-commit       # Run pre-commit hooks

# Testing
task test             # Run all tests with coverage
task test-u           # Run unit tests only

# Cleanup
task pycache          # Remove Python cache files
task ds-store         # Remove .DS_Store files
```

This guide should be updated as the project evolves and new patterns emerge. Always refer to existing code in similar
features for consistency.

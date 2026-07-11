# WalAuth

A FastAPI-based authentication service with async SQLAlchemy and JWT support.

## Tech Stack

- **FastAPI** — API framework
- **SQLAlchemy** (async) + **aiosqlite** — database layer
- **Alembic** — database migrations
- **Pydantic Settings** — typed configuration from environment variables
- **uvicorn** — ASGI server

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Getting Started

### 1. Clone and install dependencies

```bash
git clone <repository-url>
cd WalAuth
uv sync
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite+aiosqlite:///./app.db
JWT_SECRET=your-secret-key-here
```

Optional overrides (defaults shown):

```env
PROJECT_NAME=WalAuth
PORT=7007
ACCESS_TOKEN_EXPIRY=30
REFRESH_TOKEN_EXPIRY=7
```

### 3. Run the server

```bash
uv run start
```

Or with uvicorn directly:

```bash
uv run uvicorn walauth.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`. Interactive docs are at `/docs`.

## Project Structure

```
src/walauth/
├── api/          # API route handlers
├── core/         # App configuration
├── db/           # Database engine, session, and base model
├── models/       # SQLAlchemy ORM models
├── schemas/      # Pydantic request/response schemas
├── services/     # Business logic
└── main.py       # FastAPI application entry point
```

## Development

```bash
# Activate the virtual environment
source .venv/bin/activate

# Run with auto-reload
uv run uvicorn walauth.main:app --reload
```

## License

MIT

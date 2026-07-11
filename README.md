# WalAuth

A FastAPI-based authentication service with async SQLAlchemy, Alembic migrations, and JWT configuration. The project is in early development — the database layer, user model, and health check are in place; auth API routes are not yet wired up.

## Tech Stack

- **FastAPI** — API framework
- **SQLAlchemy** (async) + **aiosqlite** — database layer (SQLite)
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

Copy the example file and fill in the required values:

```bash
cp .env.example .env
```

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | — | Async SQLite connection string |
| `JWT_SECRET` | Yes | — | Secret key for signing JWTs |
| `PORT` | No | `7007` | Server port |
| `ACCESS_TOKEN_EXPIRY` | No | `30` | Access token lifetime (minutes) |
| `REFRESH_TOKEN_EXPIRY` | No | `7` | Refresh token lifetime (days) |
| `ENVIRONMENT` | No | `prod` | Set to `dev`, `development`, or `local` to enable auto-reload and SQL query logging |
| `PROJECT_NAME` | No | `WalAuth` | Application title shown in API docs |

Example `.env`:

```env
PORT=7007
DATABASE_URL=sqlite+aiosqlite:///./app.db
JWT_SECRET=your-secret-key-here
ACCESS_TOKEN_EXPIRY=30
REFRESH_TOKEN_EXPIRY=7
ENVIRONMENT=dev
```

### 3. Run database migrations

```bash
uv run alembic upgrade head
```

This creates the `users` table with `email`, `hashed_password`, `is_active`, `is_verified`, and timestamp fields.

### 4. Run the server

```bash
uv run start
```

Or with uvicorn directly:

```bash
uv run uvicorn walauth.app:app --reload --host 0.0.0.0 --port 7007
```

The API will be available at `http://localhost:7007`. Interactive docs are at `/docs`.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check; verifies database connectivity |
| `GET` | `/docs` | Swagger UI |
| `GET` | `/redoc` | ReDoc API reference |

## Project Structure

```
WalAuth/
├── alembic/              # Database migration scripts
│   └── versions/         # Individual migration revisions
├── src/walauth/
│   ├── api/              # API route handlers (not yet wired up)
│   ├── core/             # App configuration (Settings)
│   ├── db/               # Database engine, session, and base model
│   ├── models/           # SQLAlchemy ORM models (User)
│   ├── schemas/          # Pydantic request/response schemas
│   ├── services/         # Business logic
│   ├── app.py            # FastAPI app factory and routes
│   └── main.py           # CLI entry point (uvicorn)
├── alembic.ini
├── pyproject.toml
└── .env.example
```

## Development

```bash
# Activate the virtual environment
source .venv/bin/activate

# Run with auto-reload (set ENVIRONMENT=dev in .env, or pass --reload)
uv run uvicorn walauth.app:app --reload --port 7007

# Create a new migration after model changes
uv run alembic revision --autogenerate -m "describe your change"

# Apply pending migrations
uv run alembic upgrade head

# Roll back the last migration
uv run alembic downgrade -1
```

When `ENVIRONMENT` is set to `dev`, `development`, or `local`, the app enables uvicorn auto-reload and SQLAlchemy query logging automatically via `uv run start`.
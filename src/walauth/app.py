from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from walauth.core.config import settings
from walauth.db.session import engine, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="0.1.0",
        lifespan=lifespan
    )

    # app.include_router(api_router, prefix="/api/v1")

    @app.get("/health", tags=["health"])
    async def health_check(db: AsyncSession = Depends(get_db)):
        try:
            await db.execute(text("SELECT 1"))
            return {"status": "ok", "database": "connected"}
        except Exception:
            return JSONResponse(
                status_code=503,
                content={"status": "error", "database": "unreachable"},
            )

    return app

app = create_app()
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from walauth.core.config import settings
from walauth.core.exceptions import AppException
from walauth.core.logging import setup_logging
from walauth.db.session import engine, get_db

logger = logging.getLogger(settings.PROJECT_NAME)

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

    # setup_logging(settings.IS_DEV_ENV)

    @app.get("/health", tags=["health"])
    async def health_check(db: AsyncSession = Depends(get_db)):
        try:
            await db.execute(text("SELECT 1"))
            return {"status": "ok", "database": "connected"}
        except Exception as e:
            logger.error("Database health check failed", exc_info=e)
            return JSONResponse(
                status_code=503,
                content={"status": "error", "database": "unreachable"},
            )

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        logger.warning(f"{exc.__class__.__name__}: {exc.message}", extra={"path": request.url.path})
        return JSONResponse(status_code=exc.status_code, content={"error": exc.message})

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception", extra={"path": request.url.path})
        detail = str(exc) if settings.IS_DEV_ENV else "Internal server error"
        return JSONResponse(status_code=500, content={"error": detail})

    return app

app = create_app()
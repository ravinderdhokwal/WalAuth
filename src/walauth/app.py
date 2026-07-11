from contextlib import asynccontextmanager
from fastapi import FastAPI
from walauth.core.config import settings
from walauth.db.session import engine

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
    def health_check():
        return {"status": "ok"}

    return app

app = create_app()
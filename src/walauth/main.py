import uvicorn
from walauth.app import app
from walauth.core.config import settings

def main() -> None:
    uvicorn.run(
        "walauth.app:app", 
        host="0.0.0.0", 
        port=settings.PORT,
        reload=settings.IS_DEV_ENV
    )

if __name__ == "__main__":
    main()
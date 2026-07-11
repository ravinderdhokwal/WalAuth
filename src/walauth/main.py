import uvicorn
from walauth.app import app
from walauth.core.config import settings

def main() -> None:
    uvicorn.run(
        "walauth.app:app", 
        host="0.0.0.0", 
        port=settings.PORT,
        reload=True # set False in production
    )

if __name__ == "__main__":
    main()
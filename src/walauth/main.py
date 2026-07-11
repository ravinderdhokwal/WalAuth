from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)
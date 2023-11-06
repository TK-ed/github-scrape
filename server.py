from app.app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("server:app", port=6969, reload=True)
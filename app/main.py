import sys
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Add the backend root directory to Python's path before importing 'app' modules
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from app.api.v1 import chat
from app.core import config

app = FastAPI(
    title=config.PROJECT_NAME,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])

@app.get("/")
async def root():
    return {"message": f"Welcome to the {config.PROJECT_NAME} API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ask-ai")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Ask.ai Server...")
    yield 
    logger.info("Shutting down Ask.ai Server...")

app = FastAPI(
    title="Ask.ai Backend",
    description="Internal company HR and policy chatbot API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.get("/api/health", tags=["System"])
async def health_check():
    return {"status": "online", "service": "Ask.ai"}


@app.post("/api/chat", tags=["Chat"])
async def chat_endpoint(request: QueryRequest):
    user_query = request.query
    
    # Placeholder for your RAG logic:
    # 1. Get embedding for user_query
    # 2. Search MongoDB Atlas
    # 3. Call LLM (Groq/OpenAI)
    
    return {
        "query": user_query,
        "reply": "This is a placeholder response. Ask.ai is currently under construction!",
        "sources": []
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
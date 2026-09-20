from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from app.core import config

router = APIRouter()

# Define the expected request payload
class ChatRequest(BaseModel):
    query: str


client = MongoClient(config.MONGO_URI)
collection = client[config.DB_NAME][config.COLLECTION_NAME]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name=config.VECTOR_INDEX_NAME
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=config.GEMINI_API_KEY,
    temperature=0.2 # Low temperature for factual consistency
)

prompt_template = ChatPromptTemplate.from_template(
    """You are a helpful company policy assistant. 
    Answer the question using ONLY the provided context. 
    If you cannot find the answer in the context, explicitly state that you do not know.
    Do not invent or assume any company policies.
    
    Context:
    {context}
    
    Question: {question}
    
    Answer:"""
)

@router.post("/ask")
async def ask_question(request: ChatRequest):
    try:
        #top 4 most relevant chunks from MongoDB
        docs = vector_store.similarity_search(request.query, k=4)
        context_text = "\n\n---\n\n".join([doc.page_content for doc in docs])
        
        if not context_text:
            return {"answer": "I couldn't find any relevant policy documents to answer your question.", "sources": []}

        formatted_prompt = prompt_template.format(context=context_text, question=request.query)
        response = llm.invoke(formatted_prompt)
        
        
        unique_sources = list(set([doc.metadata.get("source", "Unknown") for doc in docs]))
        
        return {
            "answer": response.content,
            "sources": unique_sources
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
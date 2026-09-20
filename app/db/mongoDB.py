import os 
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()

# Database Config
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "ask_ai_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "policy_vectors")
VECTOR_INDEX_NAME = os.getenv("VECTOR_INDEX_NAME", "AskAI_index")

# AI API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# App Config
PROJECT_NAME = os.getenv("PROJECT_NAME", "Ask.ai")
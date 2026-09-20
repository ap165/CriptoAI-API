import os 

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
VECTOR_INDEX_NAME = os.getenv("VECTOR_INDEX_NAME")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PROJECT_NAME="Ask.AI"
import os 

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
VECTOR_INDEX_NAME = os.getenv("VECTOR_INDEX_NAME")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PROJECT_NAME="CRYPTO AI"

DB_NAME2 = os.getenv("DB_NAME2")
users_collection = "users" 
otp_collection = "otp"

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = 465
SMTP_USER = os.getenv("SMTP_USERNAME")
SMTP_PASS = os.getenv("SMTP_PASSWORD")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL")


JWT_SECRET = os.getenv("JWT_SECRET")
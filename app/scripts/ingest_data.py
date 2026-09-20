import os
import sys
import glob
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from app.core import config
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader, UnstructuredExcelLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient

def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".txt": return TextLoader(file_path, encoding="utf-8").load()
        elif ext == ".pdf": return PyPDFLoader(file_path).load()
        elif ext == ".docx": return Docx2txtLoader(file_path).load()
        elif ext in [".xlsx", ".xls"]: return UnstructuredExcelLoader(file_path, mode="elements").load()
        else: return []
    except Exception:
        return []

def build_pipeline():
    data_dir = os.path.join(base_dir, "app", "data", "policies")
    file_paths = glob.glob(os.path.join(data_dir, "*.*"))
    
    if not file_paths: return

    all_docs = []
    for path in file_paths:
        print(f"Loading document: {os.path.basename(path)}")
        documents = load_document(path)
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        all_docs.extend(text_splitter.split_documents(documents))

    if not all_docs: return
    
    # 1. Use the local HuggingFace embeddings! No Google API required here.
    print("Initializing HuggingFace embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 2. Connect to MongoDB Atlas
    print("Connecting to MongoDB Atlas...")
    client = MongoClient(config.MONGO_URI)
    collection = client[config.DB_NAME][config.COLLECTION_NAME]

    # 3. Push vectors to MongoDB
    print(f"Uploading chunks to MongoDB ({config.DB_NAME}.{config.COLLECTION_NAME})...")
    MongoDBAtlasVectorSearch.from_documents(
        documents=all_docs,
        embedding=embeddings,
        collection=collection,
        index_name=config.VECTOR_INDEX_NAME
    )
    
    print("✅ Ingestion pipeline completed! HuggingFace vectors are now in MongoDB.")

if __name__ == "__main__":
    build_pipeline()
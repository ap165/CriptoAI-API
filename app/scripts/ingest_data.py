import os
import sys
import json
import csv
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

base_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

if base_dir not in sys.path:
    sys.path.append(base_dir)

from app.core import config

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader,
    CSVLoader,
)

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient


# ============================================================
# Load a single document based on its file extension
# ============================================================
def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    try:
        # ----------------------------------------------------
        # TXT
        # ----------------------------------------------------
        if ext == ".txt":
            return TextLoader(
                file_path,
                encoding="utf-8"
            ).load()

        # ----------------------------------------------------
        # Markdown
        # ----------------------------------------------------
        elif ext == ".md":
            return TextLoader(
                file_path,
                encoding="utf-8"
            ).load()

        # ----------------------------------------------------
        # PDF
        # ----------------------------------------------------
        elif ext == ".pdf":
            return PyPDFLoader(file_path).load()

        # ----------------------------------------------------
        # DOCX
        # ----------------------------------------------------
        elif ext == ".docx":
            return Docx2txtLoader(file_path).load()

        # ----------------------------------------------------
        # Excel
        # ----------------------------------------------------
        elif ext in [".xlsx", ".xls"]:
            return UnstructuredExcelLoader(
                file_path,
                mode="elements"
            ).load()

        # ----------------------------------------------------
        # CSV
        # ----------------------------------------------------
        elif ext == ".csv":
            return CSVLoader(
                file_path,
                encoding="utf-8"
            ).load()

        # ----------------------------------------------------
        # JSON
        # ----------------------------------------------------
        elif ext == ".json":
            return load_json_document(file_path)

        # ----------------------------------------------------
        # Unsupported extension
        # ----------------------------------------------------
        else:
            return []

    except Exception as e:
        print(
            f"❌ Failed to load "
            f"{file_path}: {e}"
        )
        return []


# ============================================================
# Load JSON files
#
# Instead of relying on an external JSON query dependency,
# parse the JSON using Python's built-in json module.
# ============================================================
def load_json_document(file_path):

    documents = []

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        # ----------------------------------------------------
        # Pretty-print JSON so the embedding model receives
        # readable structured text.
        # ----------------------------------------------------
        formatted_json = json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        )

        documents.append(
            Document(
                page_content=formatted_json,
                metadata={
                    "source": file_path,
                    "file_type": ".json"
                }
            )
        )

        return documents

    except Exception as e:
        print(
            f"❌ Failed to parse JSON "
            f"{file_path}: {e}"
        )
        return []


# ============================================================
# Recursively discover all supported files
# ============================================================
def get_all_files(data_dir):

    supported_extensions = {
        ".txt",
        ".md",
        ".pdf",
        ".docx",
        ".xlsx",
        ".xls",
        ".csv",
        ".json",
    }

    file_paths = []

    for root, dirs, files in os.walk(data_dir):

        for file_name in files:

            file_path = os.path.join(
                root,
                file_name
            )

            ext = os.path.splitext(
                file_name
            )[1].lower()

            if ext in supported_extensions:
                file_paths.append(file_path)

    return sorted(file_paths)


# ============================================================
# Build the ingestion pipeline
# ============================================================
def build_pipeline():

    data_dir = os.path.join(
        base_dir,
        "app",
        "data",
        "policies"
    )

    print("=" * 70)
    print("VISTARA GLOBAL SYSTEMS")
    print("DOCUMENT INGESTION PIPELINE")
    print("=" * 70)

    print(
        f"\n📁 Root directory:\n{data_dir}"
    )

    # --------------------------------------------------------
    # Find all files recursively
    # --------------------------------------------------------
    file_paths = get_all_files(data_dir)

    if not file_paths:

        print(
            "\n⚠️ No supported documents were found."
        )

        return

    print(
        f"\n📚 Found {len(file_paths)} supported files."
    )

    # --------------------------------------------------------
    # Text splitter
    # --------------------------------------------------------
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    all_docs = []

    # --------------------------------------------------------
    # Load each document
    # --------------------------------------------------------
    for index, path in enumerate(
        file_paths,
        start=1
    ):

        relative_path = os.path.relpath(
            path,
            data_dir
        )

        extension = os.path.splitext(
            path
        )[1].lower()

        print(
            f"\n[{index}/{len(file_paths)}] "
            f"📄 {relative_path}"
        )

        print(
            f"   Type: {extension}"
        )

        # ----------------------------------------------------
        # Load
        # ----------------------------------------------------
        documents = load_document(path)

        if not documents:

            print(
                "   ⚠️ No content extracted."
            )

            continue

        # ----------------------------------------------------
        # Add metadata to every loaded document
        # ----------------------------------------------------
        for doc in documents:

            doc.metadata["source"] = relative_path

            doc.metadata["file_name"] = (
                os.path.basename(path)
            )

            doc.metadata["file_type"] = extension

            doc.metadata["folder"] = (
                os.path.basename(
                    os.path.dirname(path)
                )
            )

            # Relative directory
            doc.metadata["directory"] = (
                os.path.dirname(relative_path)
            )

        # ----------------------------------------------------
        # Split
        # ----------------------------------------------------
        chunks = text_splitter.split_documents(
            documents
        )

        print(
            f"   ✅ Extracted "
            f"{len(documents)} document elements"
        )

        print(
            f"   ✂️ Created "
            f"{len(chunks)} chunks"
        )

        all_docs.extend(chunks)

    # --------------------------------------------------------
    # Nothing loaded
    # --------------------------------------------------------
    if not all_docs:

        print(
            "\n⚠️ No document chunks were created."
        )

        return

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------
    print("\n" + "=" * 70)

    print(
        f"📄 Files processed: {len(file_paths)}"
    )

    print(
        f"🧩 Total chunks: {len(all_docs)}"
    )

    print("=" * 70)

    # ========================================================
    # HuggingFace embeddings
    # ========================================================
    print(
        "\n🧠 Initializing HuggingFace embeddings..."
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    print(
        "✅ Embedding model initialized."
    )

    # ========================================================
    # MongoDB Atlas
    # ========================================================
    print(
        "\n🔗 Connecting to MongoDB Atlas..."
    )

    client = MongoClient(
        config.MONGO_URI
    )

    collection = client[
        config.DB_NAME
    ][
        config.COLLECTION_NAME
    ]

    print(
        f"✅ Connected to "
        f"{config.DB_NAME}.{config.COLLECTION_NAME}"
    )

    # ========================================================
    # Upload embeddings
    # ========================================================
    print(
        "\n🚀 Uploading chunks to MongoDB Atlas..."
    )

    MongoDBAtlasVectorSearch.from_documents(
        documents=all_docs,
        embedding=embeddings,
        collection=collection,
        index_name=config.VECTOR_INDEX_NAME
    )

    # ========================================================
    # Complete
    # ========================================================
    print("\n" + "=" * 70)
    print("✅ INGESTION PIPELINE COMPLETED")
    print("=" * 70)

    print(
        f"📄 Files discovered: {len(file_paths)}"
    )

    print(
        f"🧩 Chunks uploaded: {len(all_docs)}"
    )

    print(
        f"🗄️ Database: {config.DB_NAME}"
    )

    print(
        f"📦 Collection: {config.COLLECTION_NAME}"
    )

    print(
        f"🔎 Vector Index: {config.VECTOR_INDEX_NAME}"
    )

    print("=" * 70)


# ============================================================
# Entry point
# ============================================================
if __name__ == "__main__":
    build_pipeline()
```markdown
# Company Policy RAG API

A Retrieval-Augmented Generation (RAG) backend built with FastAPI, LangChain, and MongoDB Atlas. This API ingests company documents (PDF, TXT, DOCX, Excel), converts them into searchable vector embeddings using a local HuggingFace model, and uses Google Gemini to answer user questions based strictly on the retrieved document context.

## 🚀 Tech Stack
* **Framework:** FastAPI
* **Orchestration:** LangChain
* **Vector Database:** MongoDB Atlas Vector Search
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2` / 384 dimensions)
* **LLM:** Google Gemini (`gemini-1.5-flash`)

## 📁 Project Structure
```text
backend/
├── .env                        # Secret keys and database configuration
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   └── v1/
│   │       └── chat.py         # RAG endpoint (Retrieval & Gemini Generation)
│   ├── core/
│   │   └── config.py           # Centralized environment variable loader
│   ├── data/
│   │   └── policies/           # Directory for raw documents (PDFs, TXT, etc.)
│   └── scripts/
│       └── ingest_data.py      # Script to chunk, embed, and upload data to MongoDB

```

## ⚙️ Prerequisites & Setup

### 1. Install Dependencies

Ensure you have Python installed, activate your virtual environment, and run:

```bash
pip install fastapi uvicorn pydantic python-dotenv
pip install langchain langchain-community langchain-huggingface langchain-google-genai langchain-mongodb
pip install pymongo pypdf docx2txt unstructured openpyxl sentence-transformers

```

### 2. Environment Variables

Create a `.env` file in the root `backend/` directory with the following variables:

```ini
MONGO_URI="mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority"
DB_NAME="ask_ai_db"
COLLECTION_NAME="policy_vectors"
VECTOR_INDEX_NAME="AskAI_index"
GEMINI_API_KEY="your_google_gemini_api_key"

```

### 3. Configure MongoDB Atlas Vector Index

Before ingesting data, you must create a Vector Search Index in your MongoDB Atlas dashboard.

1. Navigate to **Atlas Search** -> **Create Index** -> **Atlas Vector Search** (JSON Editor).
2. Select your database (`ask_ai_db`) and collection (`policy_vectors`).
3. Name it `AskAI_index` and use this exact JSON configuration:

```json
{
  "fields": [
    {
      "numDimensions": 384,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    }
  ]
}

```

## 🧠 Usage

### Step 1: Ingest Documents

Place your source files (PDF, TXT, DOCX, XLSX) into the `app/data/policies/` folder. Run the ingestion script from the root directory to chunk the text, generate HuggingFace embeddings, and push them to MongoDB:

```bash
python .\app\scripts\ingest_data.py

```

### Step 2: Start the FastAPI Server

Launch the backend server using Python (which will trigger Uvicorn):

```bash
python .\app\main.py

```

*Note: The server may take 10–20 seconds to boot the first time as it loads the HuggingFace embedding model into memory.*

### Step 3: Query the API

Once running, the API is available at `http://127.0.0.1:8000`. You can test the endpoint using the built-in Swagger UI at `http://127.0.0.1:8000/docs`, or send a POST request:

**Endpoint:** `POST /api/v1/chat/ask`

**Request Body:**

```json
{
  "query": "What is the company policy on remote work?"
}

```

**Response:**

```json
{
  "answer": "Employees working remotely must ensure their home networks are secure. Company-issued laptops must not be used by family members or unauthorized personnel...",
  "sources": [
    "app/data/policies/code_of_conduct.txt"
  ]
}

```

```

```
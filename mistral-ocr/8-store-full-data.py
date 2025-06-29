import json
import psycopg2
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
import logging
from tqdm import tqdm
from typing import Dict, Any
from unidecode import unidecode
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from llama_cpp import Llama
import torch  # Added import for torch

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
script_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_dir, ".env")
load_dotenv(dotenv_path)

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
SCHEMA_NAME = "eda_rag_data_e5_recursive"

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError(
        "Missing required environment variables. Please check your .env file."
    )


def get_device():
    if torch.cuda.is_available():
        return "cuda"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"


# Initialize embedding model with HuggingFace using best params
# Use the fine-tuned E5 model instead of the base model
logger.info("🚀 Loading fine-tuned E5 model for embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-base-v2",
    model_kwargs={"device": get_device(), "trust_remote_code": True},
    encode_kwargs={"normalize_embeddings": True},
)
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-mpnet-base-v2",
#     model_kwargs={"device": get_device(), "trust_remote_code": True},
#     encode_kwargs={"normalize_embeddings": True},
# )
logger.info("✅ Fine-tuned E5 model loaded successfully!")
# embeddings = llm = Llama.from_pretrained(
#     repo_id="Qwen/Qwen3-Embedding-0.6B-GGUF",
#     filename="Qwen3-Embedding-0.6B-Q8_0.gguf",
#     embedding=True,
# )
# embeddings = NVIDIAEmbeddings(
#     model="nvidia/nv-embed-v1",
#     api_key=os.getenv("NVIDIA_API_KEY"),
#     truncate="NONE",
# )

# Connection string for PGVector
connection_string = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    f"?options=-csearch_path%3D{SCHEMA_NAME}%2Cpublic"
)

# PGVector store configuration
COLLECTION_NAME = "chunks"
VECTOR_STORE_CONFIG = {
    "connection": connection_string,
    "collection_name": COLLECTION_NAME,
    "embeddings": embeddings,
    "pre_delete_collection": True,  # Keep existing embeddings
}

PROCESS_CHUNKS = True  # Disable chunk processing


def normalize_title_string(title_str: str) -> str:
    """Normalize title string by converting to lowercase ASCII."""
    if not title_str:
        return ""
    return unidecode(title_str.strip().lower())


def normalize_authors_string(authors_str: str) -> str:
    """Normalize author string by converting to lowercase ASCII."""
    if not authors_str:
        return ""
    authors = [a.strip() for a in authors_str.split(",")]
    return unidecode("; ".join(authors).lower())


def setup_database():
    """Create schema and tables if they don't exist"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()

    try:
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
        cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
        cur.execute("CREATE EXTENSION IF NOT EXISTS unaccent")
        cur.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}")
        cur.execute(f"SET search_path TO {SCHEMA_NAME}, public")

        # Check if papers table exists and is populated
        # cur.execute(
        #     f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{SCHEMA_NAME}' AND table_name = 'papers';"
        # )
        # table_exists = cur.fetchone()[0] > 0

        # if table_exists:
        #     cur.execute(f"SELECT COUNT(*) FROM {SCHEMA_NAME}.papers;")
        #     row_count = cur.fetchone()[0]

        #     if row_count > 0:
        #         logger.info(
        #             "Papers table exists and is populated. Skipping table modification."
        #         )
        #         return

        # # Create or truncate papers table

        # Always truncate papers table and restart identity
        # Check if papers table exists before truncating
        cur.execute(
            f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{SCHEMA_NAME}' AND table_name = 'papers';"
        )
        result = cur.fetchone()
        table_exists = result[0] > 0 if result else False

        if table_exists:
            cur.execute(f"TRUNCATE TABLE {SCHEMA_NAME}.papers RESTART IDENTITY;")

        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.papers (
                paper_id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                title_normalized TEXT,
                authors TEXT,
                authors_normalized TEXT,
                abstract TEXT,
                paper_link TEXT,
                year INTEGER,
                "references" JSONB,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Add indexes
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_authors_trgm ON papers USING gin (authors gin_trgm_ops)"
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_papers_abstract_trgm ON papers USING gin (abstract gin_trgm_ops)"
        )
        cur.execute(
            'CREATE INDEX IF NOT EXISTS idx_papers_references_gin ON papers USING gin ("references" jsonb_path_ops)'
        )
        cur.execute(
            'CREATE INDEX IF NOT EXISTS idx_papers_references_keys ON papers USING gin ("references")'
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_papers_year ON papers USING btree (year) WHERE year IS NOT NULL"
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_title_trgm ON papers USING gin (title gin_trgm_ops)"
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_titles_trgm ON papers USING gin (title_normalized gin_trgm_ops)"
        )

        conn.commit()
        logger.info("Database setup and indexes creation completed successfully")

    except Exception as e:
        logger.error(f"Error setting up database: {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def process_chunks(
    paper_data: Dict[str, Any], paper_id: int, vector_store: PGVector
) -> None:
    """Process and store chunks for a given paper."""
    documents = []

    for chunk in paper_data["chunks"]:
        if not chunk.get("page_content"):
            logger.warning(
                f"Skipping empty chunk {chunk.get('chunk_id', 'unknown')} for paper {paper_id}"
            )
            continue

        formulas = chunk["metadata"].get("formulas", {})

        metadata = {
            "paper_id": paper_id,
            "chunk_id": chunk["chunk_id"],  # Using pre-assigned chunk_id
            "contains_formula": bool(formulas),
            "formulas": formulas,
            "title": paper_data["paper"]["title"],
            "authors": paper_data["paper"].get("authors"),
            "year": paper_data["paper"].get("year"),
        }

        # Prepend "passage: " to the page_content for embedding
        doc = Document(
            page_content="passage: " + chunk["page_content"].strip(),
            metadata=metadata,
        )
        documents.append(doc)

    if documents:
        try:
            for doc in documents:
                print(doc.metadata["chunk_id"])  # Debugging line to check chunk_id
            vector_store.add_documents(
                documents, ids=[doc.metadata["chunk_id"] for doc in documents]
            )
            logger.info(f"Added {len(documents)} chunks for paper {paper_id}")
        except Exception as e:
            logger.error(f"Error adding chunks for paper {paper_id}: {e}")
    else:
        logger.warning(f"No valid chunks found for paper {paper_id}")


def main():
    setup_database()

    vector_store = PGVector(**VECTOR_STORE_CONFIG)

    json_path = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple_metadata_cleaned_ids.json"
    authors_path = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-improved/all_papers_data_metadata_cleaned_with_valid_authors.json"
    references_path = "/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables/extracted_references_with_proper_titles.json"

    try:
        with open(json_path, "r") as f:
            data = json.load(f)

        with open(authors_path, "r") as f:
            authors_data = json.load(f)

        with open(references_path, "r") as f:
            references_data = json.load(f)

        references_dict = {
            paper.get("metadata", {}).get("proper_title"): paper.get("references")
            for paper in references_data.get("papers", [])
        }

        authors_dict = {
            paper["paper"]["paper_id"]: paper["paper"]
            .get("valid_authors", {})
            .get("formatted_names")
            for paper in authors_data.get("papers", [])
        }

    except Exception as e:
        logger.error(f"Error loading JSON files: {e}")
        raise

    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()

    try:
        for paper_data in tqdm(data["papers"], desc="Processing papers"):
            paper = paper_data["paper"]

            title_normalized = normalize_title_string(paper["title"])
            authors_normalized = normalize_authors_string(
                authors_dict.get(paper["paper_id"], "")
            )
            references = references_dict.get(paper["title"])

            cur.execute(
                f"""
                INSERT INTO {SCHEMA_NAME}.papers (
                    title, title_normalized, authors, authors_normalized, abstract, paper_link, year, "references"
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING paper_id
                """,
                (
                    paper["title"],
                    title_normalized,
                    paper.get("authors"),
                    authors_normalized,
                    paper.get("abstract"),
                    paper.get("paper_link"),
                    paper.get("year"),
                    json.dumps(references) if references else None,
                ),
            )

            result = cur.fetchone()
            if result is None:
                logger.error(f"Failed to insert paper: {paper['title']}")
                continue

            paper_id = result[0]

            if PROCESS_CHUNKS:
                process_chunks(paper_data, paper_id, vector_store)

            conn.commit()

    except Exception as e:
        logger.error(f"Error processing papers: {e}")
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()
        logger.info("Data loading completed")


if __name__ == "__main__":
    main()

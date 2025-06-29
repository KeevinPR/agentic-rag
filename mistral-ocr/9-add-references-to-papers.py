import json
import psycopg2
import os
from dotenv import load_dotenv
import logging

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
SCHEMA_NAME = "eda_rag_data_simple"

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError(
        "Missing required environment variables. Please check your .env file."
    )


def add_references_column():
    """Add references column to papers table if it doesn't exist."""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()

    try:
        cur.execute(f"""
            ALTER TABLE {SCHEMA_NAME}.papers
            ADD COLUMN IF NOT EXISTS "references" JSONB
        """)
        conn.commit()
        logger.info("Added references column to papers table.")
    except Exception as e:
        logger.error(f"Error adding references column: {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def update_references():
    """Update papers table with references from JSON file."""
    json_path = "/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables/extracted_references.json"
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Error loading JSON file: {e}")
        raise

    if not isinstance(data, dict) or "papers" not in data:
        raise ValueError("Invalid JSON structure: expected 'papers' key in root object")

    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()

    try:
        for paper_data in data["papers"]:
            title = paper_data.get("metadata", {}).get("title")
            references = paper_data.get("references")

            if not title or not references:
                logger.warning("Skipping paper with missing title or references.")
                continue

            try:
                cur.execute(
                    f"""
                    UPDATE {SCHEMA_NAME}.papers
                    SET "references" = %s
                    WHERE title = %s
                    """,
                    (json.dumps(references), title),
                )
                conn.commit()
                logger.info(f"Updated references for paper titled '{title}'.")
            except Exception as e:
                logger.error(
                    f"Error updating references for paper titled '{title}': {e}"
                )
                conn.rollback()

    except Exception as e:
        logger.error(f"Error in updating references: {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
        logger.info("References update completed.")


def main():
    add_references_column()
    update_references()


if __name__ == "__main__":
    main()

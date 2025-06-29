# mistral-ocr: Data Processing & Extraction

This folder contains all scripts for data extraction, processing, and chunking used to build the knowledge base for the Agentic RAG system.

## 📦 What is in this folder?
- **PDF OCR & Extraction**: Scripts to extract text, images, and metadata from PDFs
- **Chunking & Preprocessing**: Scripts to split, clean, and augment document content
- **Metadata & Reference Handling**: Utilities for normalizing, mapping, and enriching paper metadata
- **Configurable Paths**: Most scripts require you to set the correct input/output paths. Use the provided `config.py` for relative, portable paths across environments.
- **Database Setup**: The `eda-rag-db/` subfolder contains the Docker setup for launching a PostgreSQL database with the pgvector extension, used as the vector database backend for the Agentic RAG system.

## ⚙️ Usage Notes
- **Path Configuration**: Many scripts require you to specify input/output directories.
- **Environment**: Install dependencies from `environment.yml` to ensure all scripts run smoothly.
- **Data Storage**: Processed data, chunked markdown, and intermediate files are stored in subfolders according to the pipeline stage.

## 🗄️ Subfolders
- `eda-rag-db/`: Docker setup for the pgvector database backend
- `chunked-markdown-*`: Various chunking strategies and outputs
- `evaluate-dataset/`, `scrape/`, etc.: Additional utilities and data pipelines

## 📝 Typical Workflow
1. Place your raw PDFs in the appropriate data directory
2. Run the OCR and extraction scripts to generate markdown and images
3. Use chunking and cleaning scripts to prepare data for retrieval
4. Store and index the processed data in the pgvector database (see `eda-rag-db/`)

---

*This folder is the heart of the data pipeline for your Agentic RAG system. Configure your paths, process your data, and power your knowledge base!* 

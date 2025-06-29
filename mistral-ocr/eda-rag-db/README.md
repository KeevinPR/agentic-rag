# eda-rag-db: pgvector Database Container

This folder contains the Docker setup for launching a PostgreSQL database with the pgvector extension. It is used as the vector database backend for the Agentic RAG system.

---

Need to create a .env.local file with the variables shown in .env.example

## 🚀 Quick Start

1. **Start the database container:**
   ```bash
   docker compose up -d
   ```
   This will launch the PostgreSQL database in the background.

2. **Connect to the database:**
   You can use any PostgreSQL client, for example:
   ```bash
   psql -h localhost -U <your_user> -d <your_db>
   ```
   (Replace `<your_user>` and `<your_db>` with your credentials from `.env.local`)

3. **Enable the pgvector extension:**
   Once connected to your database, run:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```
   This command enables the pgvector extension required for vector search.

---

*This setup provides the vector database backend for your Agentic RAG system.*
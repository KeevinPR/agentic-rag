# Agentic RAG System for Estimation of Distribution Algorithms

An intelligent document processing and retrieval system that combines OCR processing with Retrieval-Augmented Generation (RAG) capabilities.

## 🏗️ Repository Structure

```
agentic-rag/
├── chainlit/              # Agentic RAG execution and user interface
├── mistral-ocr/          # Raw data extraction and processing scripts
├── data/                 # PDF knowledge database
└── README.md
```

### 📁 Directory Overview

#### `/chainlit/`
Contains the core Agentic RAG system with interactive user interface:
- **Purpose**: Main application for document querying and AI-powered responses
- **Features**: Interactive chat interface, document retrieval, and intelligent answer generation
- **Technology**: Built with Chainlit for seamless UI/UX

#### `/mistral-ocr/`
Houses data processing and extraction scripts:
- **Purpose**: Convert raw PDF documents into structured, searchable format
- **Features**: OCR processing, image extraction, markdown conversion
- **Technology**: Powered by Mistral AI's OCR capabilities
- **Output**: Processed documents ready for RAG ingestion

#### `/data/`
Centralized repository for source documents:
- **Purpose**: Storage for all PDF files used in the knowledge database
- **Content**: Research papers, documents, and reference materials
- **Format**: PDF files that get processed by the OCR pipeline

---

*Built for efficient document processing and intelligent information retrieval.* 
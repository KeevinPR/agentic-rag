"""
Search and utility tools for the EDA research assistant.
"""

import logging
import json
from pathlib import Path
import re
import textwrap
from typing import List, Optional, Dict, Any, Tuple
from unidecode import unidecode
import httpx
import os

from langchain_core.tools import tool
from langchain_tavily import TavilySearch
import asyncio
from config import SEARCH_CONFIG, LLM_CONFIG_GOOGLE
from utils import (
    init_vector_stores,
    get_pg_pool,
)
from prompts import (
    SQL_GENERATION_PROMPT,
)
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# Initialize the cross-encoder model once
# cross_encoder = CrossEncoder(SEARCH_CONFIG["cross_encoder"]["model_name"])

# Constants for web search formatting
WRAP_WIDTH = 1000  # ~8-10 tweet-lengths
DEFAULT_LIMIT = 10
MAX_LIMIT = 50
QUERY_TIMEOUT = 30


@tool
async def hybrid_search_tool(
    raw_user_query: str,  # Add raw user query parameter
    llm_query: str,
    paper_title: Optional[str] = None,
    algorithm_names: Optional[List[str]] = None,
    is_latex_query: Optional[bool] = False,
) -> str:
    """
    Enhanced hybrid semantic and algorithm search tool for the academic paper database.
    Uses RRF (Reciprocal Rank Fusion) with cross-encoder re-ranking for improved relevance.

    Args:
        raw_user_query: Original raw user query
        llm_query: The LLM-processed search query (keywords/concepts)
        paper_title: Optional paper title to filter results to a specific paper
        algorithm_names: Specific algorithm names included in the query (determined by LLM)
        is_latex_query: User asking for formulas or equations


    Use this tool for:
    - General, open-ended, or semantic searches about EDAs
    - Questions containing formulas or algorithms
    - Paper-specific content searches when paper_id or paper_title is provided
    - Detailed content analysis of specific papers

    Examples:
    - llm_query="EDAs types", raw_user_query="What are the main types of EDAs?", algorithm_names=EDA, is_latex_query=False
    - llm_query="UMDA LaTeX formula", raw_user_query="Show me the LaTeX code for UMDA", algorithm_names=UMDA, is_latex_query=True
    - llm_query="concept XX paper YY", raw_user_query="Can you expand the concept XX in paper YY?", is_latex_query=False
    """
    try:
        logger.info(f"Starting enhanced hybrid search")
        logger.info(f"Processed query: {llm_query}")
        logger.info(f"Raw user query: {raw_user_query}")
        if paper_title:
            logger.info(f"Filtering results to paper_title: {paper_title}")

        vector_store = init_vector_stores()

        # Optimized retrieval counts based on best practices
        semantic_candidates = 20  # Reduced for better precision
        fts_candidates = 15  # Smaller for focused FTS results
        final_rerank_candidates = 25  # Total to rerank
        num_results = 5

        # Fixed weights based on Anthropic contextual embeddings best practices
        semantic_weight = 0
        fts_weight = 1

        logger.info(
            f"Retrieval strategy: {semantic_candidates} semantic + {fts_candidates} FTS -> {final_rerank_candidates} rerank -> {num_results} final"
        )

        all_embedding_docs = {}
        all_fts_rows = []

        pool = await get_pg_pool()

        filter_dict = {}
        if paper_title:
            filter_dict["title"] = paper_title

        # Semantic search using processed query (better for embeddings)
        embedding_results = vector_store.similarity_search_with_score(
            f"query: {llm_query}", k=semantic_candidates, filter=filter_dict
        )
        # embedding_results = vector_store.similarity_search_with_score(
        #     llm_query, k=semantic_candidates, filter=filter_dict
        # )
        logger.info(f"Found {len(embedding_results)} results from vector search")
        for doc, score in embedding_results:
            chunk_id = doc.metadata["chunk_id"]
            if (
                chunk_id not in all_embedding_docs
                or score > all_embedding_docs[chunk_id][1]
            ):
                all_embedding_docs[chunk_id] = (doc, score)

        # BM25-like FTS search using raw user query for natural language processing
        search_query = raw_user_query if raw_user_query else llm_query
        await _perform_bm25_like_fts_search(
            pool,
            search_query,  # Use raw user query for natural language FTS
            llm_query,  # Use processed query for fallback term extraction
            algorithm_names,
            is_latex_query,
            paper_title,
            fts_candidates,
            all_fts_rows,
        )

        logger.info(f"Found {len(all_embedding_docs)} unique vector results")
        logger.info(f"Found {len(all_fts_rows)} unique FTS results")

        # RRF Scoring with fixed weights
        logger.info("Calculating RRF scores...")
        embedding_ranks = {
            chunk_id: idx
            for idx, (chunk_id, _) in enumerate(all_embedding_docs.items())
        }
        fts_ranks = {row["id"]: idx for idx, row in enumerate(all_fts_rows)}

        rrf_k = 60  # Standard RRF parameter
        all_chunk_ids = set(all_embedding_docs.keys()) | set(fts_ranks.keys())
        rrf_scores = {}

        for chunk_id in all_chunk_ids:
            rank_embedding = embedding_ranks.get(chunk_id)
            rank_fts = fts_ranks.get(chunk_id)
            score = 0
            if rank_embedding is not None:
                score += semantic_weight / (rrf_k + rank_embedding + 1)
            if rank_fts is not None:
                score += fts_weight / (rrf_k + rank_fts + 1)
            rrf_scores[chunk_id] = score

        # Get top candidates for reranking
        initial_top_chunks = sorted(
            rrf_scores.items(), key=lambda x: x[1], reverse=True
        )[:final_rerank_candidates]

        # Prepare candidate documents
        candidate_docs = await _prepare_candidate_docs(
            initial_top_chunks, all_embedding_docs, all_fts_rows
        )

        # Cross-encoder reranking (use raw user query for better context understanding)
        rerank_query = raw_user_query if raw_user_query else llm_query
        if len(candidate_docs) >= 5:  # Only rerank if we have enough candidates
            candidate_docs = await _perform_reranking(rerank_query, candidate_docs)

        # Select final results
        final_count = min(num_results, len(candidate_docs))
        final_chunk_ids = [doc["id"] for doc in candidate_docs[:final_count]]
        results = []

        for i, doc in enumerate(candidate_docs[:final_count]):
            score_info = f"RRF:{doc.get('score', 0):.3f}"
            if "rerank_score" in doc:
                score_info += f", Rerank:{doc['rerank_score']:.3f}"

            logger.info(f"Result {i + 1}: {score_info}")
            formatted_content = f"Chunk {i + 1}:\n{doc['content']}\n"
            results.append(
                {
                    "content": formatted_content,
                    "metadata": doc["metadata"],
                    "score": doc.get("rerank_score", doc.get("score", 0.0)),
                }
            )

        # Formula processing
        await _process_formula_placeholders(results)

        total_chars = sum(len(str(r)) for r in results)
        logger.info(
            f"Enhanced search complete: {len(results)} results, {total_chars} chars total"
        )

        final_output = (
            "Here are the top search results for your query:\n\n"
            + "\n".join([r["content"] for r in results])
        )

        _append_chunk_ids_to_json(
            llm_query, [cid for cid, _ in initial_top_chunks], final_chunk_ids
        )

        return final_output

    except Exception as e:
        logger.error(f"Error in enhanced hybrid_search_tool: {str(e)}", exc_info=True)
        raise


async def _perform_bm25_like_fts_search(
    pool,
    raw_query,  # Raw user query for natural language processing
    processed_query,  # LLM-extracted keywords for fallback strategies
    algorithm_names,
    is_latex_query,
    paper_title,
    fts_candidates,
    all_fts_rows,
):
    """
    Improved FTS search that mimics BM25 behavior with intelligent query routing.

    Args:
        raw_query: Original user question for websearch_to_tsquery
        processed_query: LLM-extracted keywords for fallback strategies
    """
    formula_filter = (
        "AND cmetadata->>'contains_formula' = 'true'" if is_latex_query else ""
    )
    paper_filter = ""
    if paper_title:
        escaped_title = paper_title.replace("'", "''")
        paper_filter = f"AND cmetadata->>'title' = '{escaped_title}'"

    # Strategy 1: Precise algorithm search (if provided)
    if algorithm_names:
        await _fts_algorithm_search_precise(
            pool,
            algorithm_names,
            formula_filter,
            paper_filter,
            fts_candidates,
            all_fts_rows,
        )

    # Strategy 2: Natural language search using raw user query
    await _fts_natural_language_search(
        pool,
        raw_query,
        processed_query,
        formula_filter,
        paper_filter,
        fts_candidates,
        all_fts_rows,
    )


async def _fts_algorithm_search_precise(
    pool, algorithm_names, formula_filter, paper_filter, fts_candidates, all_fts_rows
):
    """
    Precise algorithm search using exact matching and phrase queries.
    """
    try:
        # Filter and prepare algorithm terms more precisely
        precise_terms = []
        for name in algorithm_names:
            name = name.strip()
            if len(name) >= 2:  # Keep even short algorithm names like "GA", "DE"
                # For multi-word algorithm names, use phrase search
                if " " in name:
                    # Convert to phrase query: "Univariate Marginal Distribution Algorithm"
                    words = name.split()
                    phrase = " <-> ".join(
                        words
                    )  # Use phrase operator for exact sequence
                    precise_terms.append(f"({phrase})")
                else:
                    # Single word - use exact term with possible prefix matching
                    precise_terms.append(f"{name}:*")

        if not precise_terms:
            return

        # Use OR logic for multiple algorithms, but maintain precision within each
        fts_query = " | ".join(precise_terms)
        logger.info(f"Precise algorithm FTS query: {fts_query}")

        async with pool.acquire() as conn:
            fts_rows = await conn.fetch(
                f"""
                SELECT id, document, cmetadata,
                    ts_rank_cd(
                        to_tsvector('english', document),
                        to_tsquery('english', $1),
                        32  -- Use cover density ranking for better BM25-like behavior
                    ) AS fts_score
                FROM eda_rag_data_augmented_e5.langchain_pg_embedding
                WHERE to_tsvector('english', document)
                    @@ to_tsquery('english', $1)
                    {formula_filter}
                    {paper_filter}
                ORDER BY fts_score DESC
                LIMIT $2;
                """,
                fts_query,
                fts_candidates,
            )

            logger.info(f"Precise algorithm FTS returned {len(fts_rows)} results")
            _merge_fts_results_with_scores(fts_rows, all_fts_rows)

    except Exception as e:
        logger.warning(f"Precise algorithm FTS failed with query '{fts_query}': {e}")


async def _fts_natural_language_search(
    pool,
    raw_query,
    processed_query,
    formula_filter,
    paper_filter,
    fts_candidates,
    all_fts_rows,
):
    """
    Natural language search with intelligent fallback strategies.
    """
    if not raw_query or not raw_query.strip():
        return

    async with pool.acquire() as conn:
        # Primary strategy: websearch_to_tsquery with raw user query (best for natural language)
        success = await _try_websearch_bm25(
            conn, raw_query, formula_filter, paper_filter, fts_candidates, all_fts_rows
        )

        if success:
            return

        # Fallback: Intelligent term extraction using processed query
        await _try_intelligent_term_search(
            conn,
            processed_query,
            formula_filter,
            paper_filter,
            fts_candidates,
            all_fts_rows,
        )


async def _try_websearch_bm25(
    conn, raw_query, formula_filter, paper_filter, limit, all_fts_rows
):
    """
    Try websearch_to_tsquery with raw user query for natural language processing.
    Uses BM25-like ranking with cover density.
    """
    try:
        logger.info(f"Trying websearch FTS with raw query: '{raw_query}'")

        fts_rows = await conn.fetch(
            f"""
            SELECT id, document, cmetadata,
                ts_rank_cd(
                    to_tsvector('english', document),
                    websearch_to_tsquery('english', $1),
                    32  -- Cover density ranking for BM25-like behavior
                ) AS fts_score
            FROM eda_rag_data_augmented_e5.langchain_pg_embedding
            WHERE to_tsvector('english', document)
                @@ websearch_to_tsquery('english', $1)
            {formula_filter}
            {paper_filter}
            ORDER BY fts_score DESC
            LIMIT $2;
            """,
            raw_query,
            limit,
        )

        if fts_rows:
            logger.info(f"Websearch BM25 returned {len(fts_rows)} results")
            _merge_fts_results_with_scores(fts_rows, all_fts_rows)
            return True
        else:
            logger.info("Websearch FTS returned no results, trying fallback")
            return False

    except Exception as e:
        logger.warning(f"Websearch BM25 failed: {e}")
        return False


async def _try_intelligent_term_search(
    conn, processed_query, formula_filter, paper_filter, limit, all_fts_rows
):
    """
    Intelligent term extraction that creates focused AND queries instead of broad OR queries.
    Uses the LLM-processed query which should have better keywords.
    """
    try:
        # Enhanced stop words for academic content
        stop_words = {
            "what",
            "are",
            "is",
            "the",
            "of",
            "and",
            "or",
            "to",
            "in",
            "for",
            "with",
            "how",
            "why",
            "when",
            "who",
            "which",
            "can",
            "you",
            "show",
            "me",
            "explain",
            "describe",
            "find",
            "get",
            "give",
            "tell",
            "about",
            "this",
            "that",
            "these",
            "those",
            "algorithm",
            "algorithms",
            "method",
            "methods",
            "approach",
            "technique",
            "use",
            "used",
            "using",
            "paper",
            "study",
            "research",
            "analysis",
        }

        # Extract meaningful terms from processed query
        import re

        # Split on word boundaries and clean
        raw_terms = re.findall(r"\b[a-zA-Z]+\b", processed_query.lower())

        meaningful_terms = []
        for term in raw_terms:
            if len(term) >= 3 and term not in stop_words and not term.isdigit():
                meaningful_terms.append(term)

        if len(meaningful_terms) == 0:
            logger.info("No meaningful terms extracted from processed query")
            return

        # Create focused query strategy
        if len(meaningful_terms) <= 3:
            # For short queries, require ALL terms (AND logic)
            tsquery_str = " & ".join(meaningful_terms)
        else:
            # For longer queries, use the most important terms with AND
            # Take first 3-4 terms (usually the most important)
            important_terms = meaningful_terms[:4]
            tsquery_str = " & ".join(important_terms)

        logger.info(
            f"Intelligent FTS query: '{tsquery_str}' (from terms: {meaningful_terms})"
        )

        fts_rows = await conn.fetch(
            f"""
            SELECT id, document, cmetadata,
                ts_rank_cd(
                    to_tsvector('english', document),
                    to_tsquery('english', $1),
                    32  -- Cover density ranking for BM25-like behavior
                ) AS fts_score
            FROM eda_rag_data_augmented_e5.langchain_pg_embedding
            WHERE to_tsvector('english', document)
                @@ to_tsquery('english', $1)
            {formula_filter}
            {paper_filter}
            ORDER BY fts_score DESC
            LIMIT $2;
            """,
            tsquery_str,
            limit,
        )

        logger.info(f"Intelligent term search returned {len(fts_rows)} results")
        _merge_fts_results_with_scores(fts_rows, all_fts_rows)

    except Exception as e:
        logger.warning(f"Intelligent term search failed: {e}")


def _merge_fts_results_with_scores(new_rows, all_fts_rows):
    """
    Merge FTS results while preserving scores for proper ranking.
    """
    existing_ids = {row["id"] for row in all_fts_rows}
    for row in new_rows:
        if row["id"] not in existing_ids:
            # Convert asyncpg Record to dict and ensure fts_score is included
            row_dict = dict(row)
            all_fts_rows.append(row_dict)
            existing_ids.add(row["id"])


async def _prepare_candidate_docs(initial_top_chunks, all_embedding_docs, all_fts_rows):
    """
    Prepare candidate documents with improved error handling and metadata extraction.
    """
    candidate_docs = []

    for chunk_id, rrf_score in initial_top_chunks:
        doc, _ = all_embedding_docs.get(chunk_id, (None, None))

        if doc:
            metadata_context = _extract_metadata_context(doc.metadata)
            candidate_docs.append(
                {
                    "id": chunk_id,
                    "content": doc.page_content,
                    "metadata_context": metadata_context,
                    "metadata": doc.metadata,
                    "score": rrf_score,
                    "source": "vector",
                }
            )
        else:
            # Try to find in FTS results
            row = next((r for r in all_fts_rows if r["id"] == chunk_id), None)
            if row:
                metadata = _parse_metadata(row["cmetadata"])
                metadata_context = _extract_metadata_context(metadata)

                candidate_docs.append(
                    {
                        "id": chunk_id,
                        "content": row["document"],
                        "metadata_context": metadata_context,
                        "metadata": metadata,
                        "score": rrf_score,
                        "source": "fts",
                    }
                )

    return candidate_docs


def _extract_metadata_context(metadata):
    """Extract useful context from metadata for better reranking."""
    if not isinstance(metadata, dict):
        return ""

    context_parts = []
    if "source" in metadata:
        context_parts.append(f"Source: {metadata['source']}")
    if "title" in metadata:
        context_parts.append(f"Title: {metadata['title']}")

    return "\n".join(context_parts) + ("\n" if context_parts else "")


def _parse_metadata(metadata):
    """Safely parse metadata that might be a string or dict."""
    if isinstance(metadata, dict):
        return metadata
    elif isinstance(metadata, str):
        try:
            return json.loads(metadata)
        except json.JSONDecodeError:
            logger.warning(f"Could not parse metadata as JSON: {metadata}")
            return {}
    else:
        return {}


async def _perform_reranking(query, candidate_docs):
    """
    Improved cross-encoder reranking with better score handling.
    Now uses Jina AI API instead of local CrossEncoder.
    The old implementation is commented out below for reference.
    """
    logger.info("Performing reranking using Jina AI API...")
    jina_api_key = os.getenv("JINA_API_KEY")
    if not jina_api_key:
        logger.warning(
            "JINA_API_KEY not found. Skipping reranking. For better results, please set the JINA_API_KEY environment variable."
        )
        return candidate_docs

    try:
        documents = [doc["content"] for doc in candidate_docs]

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.jina.ai/v1/rerank",
                headers={
                    "Authorization": f"Bearer {jina_api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "jina-reranker-v2-base-en",
                    "query": query,
                    "documents": documents,
                    "top_n": len(documents),
                },
                timeout=30.0,
            )
            response.raise_for_status()
            rerank_results = response.json()["results"]

        # Apply reranking scores to all documents
        for i, doc in enumerate(candidate_docs):
            # Find the corresponding result
            res = next(
                (r for r in rerank_results if r["index"] == i),
                None,
            )
            if res:
                doc["rerank_score"] = res["relevance_score"]
            else:
                doc["rerank_score"] = 0.0  # Should not happen if top_n is set correctly

        # Sort by rerank score (highest first)
        candidate_docs.sort(key=lambda x: x["rerank_score"], reverse=True)

        # Optional: Filter out very low relevance scores (adjust threshold as needed)
        score_threshold = 0.5  # More lenient threshold to avoid over-filtering
        filtered_docs = [
            doc for doc in candidate_docs if doc["rerank_score"] >= score_threshold
        ]

        if filtered_docs:
            logger.info(
                f"Reranking complete: {len(filtered_docs)}/{len(candidate_docs)} above threshold {score_threshold}"
            )
            return filtered_docs
        else:
            logger.info("No docs above threshold, returning all reranked results")
            return candidate_docs

    except httpx.TimeoutException:
        logger.warning("Jina AI reranking timed out, using original ranking")
        return candidate_docs
    except httpx.HTTPStatusError as e:
        logger.error(
            f"Jina AI reranking failed with HTTP status {e.response.status_code}: {e.response.text}, using original ranking"
        )
        return candidate_docs
    except Exception as e:
        logger.error(f"Jina AI reranking failed: {e}, using original ranking")
        return candidate_docs

    # --- OLD CrossEncoder logic is preserved below for reference ---
    # logger.info("Performing cross-encoder re-ranking...")
    #
    # try:
    #     # Prepare pairs for the reranker (query should be the original user intent)
    #     rerank_pairs = [(query, doc["content"]) for doc in candidate_docs]
    #
    #     # Get scores from cross-encoder with timeout protection
    #     rerank_scores = await asyncio.wait_for(
    #         asyncio.to_thread(cross_encoder.predict, rerank_pairs),
    #         timeout=30.0,
    #     )
    #
    #     # Apply reranking scores to all documents
    #     for i, doc in enumerate(candidate_docs):
    #         doc["rerank_score"] = float(rerank_scores[i])
    #
    #     # Sort by rerank score (highest first)
    #     candidate_docs.sort(key=lambda x: x["rerank_score"], reverse=True)
    #
    #     # Optional: Filter out very low relevance scores (adjust threshold as needed)
    #     score_threshold = 0.5  # More lenient threshold to avoid over-filtering
    #     filtered_docs = [
    #         doc for doc in candidate_docs if doc["rerank_score"] >= score_threshold
    #     ]
    #
    #     if filtered_docs:
    #         logger.info(
    #             f"Reranking complete: {len(filtered_docs)}/{len(candidate_docs)} above threshold {score_threshold}"
    #         )
    #         return filtered_docs
    #     else:
    #         logger.info("No docs above threshold, returning all reranked results")
    #         return candidate_docs
    #
    # except asyncio.TimeoutError:
    #     logger.warning("Cross-encoder reranking timed out, using original ranking")
    #     return candidate_docs
    # except Exception as e:
    #     logger.error(f"Cross-encoder reranking failed: {e}, using original ranking")
    #     return candidate_docs


async def _process_formula_placeholders(results):
    """Process formula placeholders with improved error handling."""
    logger.info("Processing formula placeholders...")

    for i, result in enumerate(results):
        try:
            content = result["content"]
            metadata = _parse_metadata(result["metadata"])

            if not isinstance(metadata, dict) or "formulas" not in metadata:
                continue

            formulas = metadata["formulas"]
            if not isinstance(formulas, dict):
                continue

            logger.info(f"Found {len(formulas)} formulas in result {i + 1}")

            # Create comprehensive placeholder mapping
            placeholder_mapping = {}
            for placeholder, formula in formulas.items():
                if not isinstance(formula, str):
                    continue

                # Handle various placeholder formats
                normalized_formats = _normalize_placeholder_formats(placeholder)
                for fmt in normalized_formats:
                    placeholder_mapping[fmt] = formula

            # Replace placeholders (longest first to avoid partial replacements)
            content = _replace_placeholders(content, placeholder_mapping)
            result["content"] = content

        except Exception as e:
            logger.warning(f"Error processing formulas in result {i + 1}: {e}")


def _normalize_placeholder_formats(placeholder):
    """Generate different placeholder format variations for backward compatibility."""
    formats = [placeholder]  # Original format

    # Handle [FORMULA_X] vs [FORMULAX] variations
    if placeholder.startswith("[FORMULA_"):
        base_format = placeholder.replace("_", "")
        formats.append(base_format)
    elif placeholder.startswith("[FORMULA") and "_" not in placeholder:
        underscore_format = placeholder.replace("[FORMULA", "[FORMULA_")
        formats.append(underscore_format)

    return formats


def _replace_placeholders(content, placeholder_mapping):
    """Replace formula placeholders in content."""
    # Sort by length (longest first) to avoid partial replacements
    sorted_placeholders = sorted(placeholder_mapping.keys(), key=len, reverse=True)

    for placeholder in sorted_placeholders:
        if placeholder in content:
            formula = placeholder_mapping[placeholder]
            content = content.replace(placeholder, formula)
            logger.debug(f"Replaced '{placeholder}' with formula")

    return content


def _append_chunk_ids_to_json(
    query: str,
    initial_ids: List[str],
    final_ids: List[str],
    json_file_path: str = "hybrid_search_chunk_ids.json",
) -> None:
    """Append a search's chunk IDs to ``json_file_path``."""

    entry = {
        "query": query,
        "initial_candidate_ids": initial_ids,
        "final_chunk_ids": final_ids,
    }

    path = Path(json_file_path)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            try:
                existing = json.load(f)
                if not isinstance(existing, list):
                    existing = []
            except json.JSONDecodeError:
                existing = []
    else:
        existing = []

    existing.append(entry)

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    logger.info("Search chunk IDs logged to %s", path)


@tool
async def web_search_tool(query: str) -> str:
    """
    Search the web for information using Tavily API with compact, readable Markdown output.
    Args:
        query: The search query
    Returns:
        Formatted search results as a string with highlighted query terms
    """
    try:
        logger.info("Processing web search query: %s", query)
        tavily_search = TavilySearch(
            max_results=5,
            include_raw_content=True,
        )
        results = await tavily_search.ainvoke(query)

        # Handle no results case
        if not results.get("results"):
            return "No results found for your query."

        out_lines = []

        # Add quick answer if available
        answer = results.get("answer")
        if answer:
            out_lines.append(f"**Quick answer:** {answer}\n")

        # Pre-compile regex for highlighting query terms
        terms = [re.escape(t) for t in query.split()]
        regex = re.compile(r"(" + "|".join(terms) + r")", flags=re.I)

        # Process each result
        for idx, res in enumerate(results["results"], 1):
            # Extract fields according to Tavily's response format
            title = res.get("title", "No title")
            url = res.get("url", "No URL")
            content = res.get("content", "No content")
            score = res.get("score", 0)

            # Clean and shorten content
            content = " ".join(content.split())
            snippet = textwrap.shorten(content, width=WRAP_WIDTH, placeholder="…")

            # Highlight query terms in snippet
            snippet = regex.sub(r"`\1`", snippet)

            # Format result in Markdown with score
            out_lines.append(
                f"### Result {idx} (Score: {score:.2f})\n"
                f"- **{title}**\n"
                f"- <{url}>\n"
                f"- {snippet}\n"
            )

        # Add response time if available
        response_time = results.get("response_time")
        if response_time:
            out_lines.append(f"\n*Search completed in {response_time:.2f} seconds*")

        return "\n".join(out_lines)

    except Exception as exc:
        logger.error("Error in web_search_tool: %s", exc, exc_info=True)
        return f"Sorry—search failed ({exc.__class__.__name__})."


def enhance_sql_generation_parameters(**params) -> Dict[str, Any]:
    """Enhance parameters for better SQL generation"""
    enhanced_params = params.copy()

    # Add query analysis hints
    query = params.get("query", "")
    query_lower = query.lower()
    print(query_lower)

    # Detect if user wants recent papers
    if any(term in query_lower for term in ["recent", "latest", "new", "current"]):
        enhanced_params["prioritize_recent"] = True

    # Detect if user wants comprehensive results
    if any(
        term in query_lower
        for term in ["all", "comprehensive", "complete", "everything"]
    ):
        enhanced_params["comprehensive_search"] = True

    # Detect specific result size requests
    size_patterns = [
        (r"(\d+)\s*papers?", lambda m: int(m.group(1))),
        (r"top\s*(\d+)", lambda m: int(m.group(1))),
        (r"first\s*(\d+)", lambda m: int(m.group(1))),
    ]

    for pattern, extractor in size_patterns:
        match = re.search(pattern, query_lower)
        if match:
            requested_count = extractor(match)
            enhanced_params["requested_limit"] = min(requested_count, MAX_LIMIT)
            break

    return enhanced_params


def format_summary_results(result, total_count: int) -> str:
    """Format large result sets with summary view"""
    display_count = min(len(result), 20)  # Show max 20 in summary

    summary = f"Found {total_count} papers. Showing first {display_count}:\n\n"

    for i, row in enumerate(result[:display_count]):
        title = row.get("title", "Unknown Title")
        year = row.get("year", "Unknown Year")
        authors = row.get("authors", "Unknown Authors")

        # Truncate long titles and author lists for summary
        title_short = title[:80] + "..." if len(title) > 80 else title
        authors_short = authors[:50] + "..." if len(authors) > 50 else authors

        summary += f"{i + 1}. {title_short} ({year}) - {authors_short}\n"

    if len(result) > display_count:
        summary += f"\n... and {len(result) - display_count} more results"

    summary += f"\n\nFor detailed information, try a more specific query or request a smaller subset."

    return summary


def format_standard_results(result, include_refs: bool) -> str:
    """Format standard result set"""
    rows = []
    for row in result:
        title = row.get("title", "Unknown Title")
        year = row.get("year", "Unknown Year")
        authors = row.get("authors", "Unknown Authors")
        link = row.get("paper_link", "No Link")
        abstract = row.get("abstract", "No Abstract")

        line = f"TITLE: {title}; YEAR: {year}; AUTHORS: {authors}; LINK: {link}; ABSTRACT: {abstract}"

        if include_refs and "references" in row and row["references"]:
            refs = row["references"]
            # Format references nicely for standard results
            if isinstance(refs, (dict, list)):
                import json

                refs_formatted = json.dumps(refs, indent=2, ensure_ascii=False)
                line += f"; REFERENCES: {refs_formatted}"
            else:
                line += f"; REFERENCES: {refs}"

        rows.append(line)

    return "\n".join(rows)


def format_detailed_result(row, include_refs: bool) -> str:
    """Format single result with full details"""
    title = row.get("title", "Unknown Title")
    year = row.get("year", "Unknown Year")
    authors = row.get("authors", "Unknown Authors")
    link = row.get("paper_link", "No Link")
    abstract = row.get("abstract", "No Abstract")

    result = f"TITLE: {title}; YEAR: {year}; AUTHORS: {authors}; LINK: {link}; ABSTRACT: {abstract}"

    if include_refs and "references" in row and row["references"]:
        refs = row["references"]
        # Format references nicely
        if isinstance(refs, (dict, list)):
            import json

            refs_formatted = json.dumps(refs, indent=2, ensure_ascii=False)
            result += f"; REFERENCES: {refs_formatted}"
        else:
            result += f"; REFERENCES: {refs}"

    return result


def format_results_intelligently(
    result, include_refs: bool, estimated_total: int | None = None
) -> str:
    """Format results based on size and content with intelligent adaptation"""

    if not result:
        return "No results found"

    result_count = len(result)

    # Single result: provide full details
    if result_count == 1:
        return format_detailed_result(result[0], include_refs)

    # Small result set: standard format
    elif result_count <= 10:
        return format_standard_results(result, include_refs)

    # Large result set: summary format
    else:
        return format_summary_results(result, estimated_total or result_count)


async def estimate_result_size(sql_query: str, conn, timeout: int = 10) -> int:
    """Estimate result size before full execution"""
    try:
        # Convert to count query for estimation
        sql_query = sql_query.rstrip("; \n")
        count_query = f"SELECT COUNT(*) FROM ({sql_query}) AS estimate_subquery"
        result = await asyncio.wait_for(conn.fetchval(count_query), timeout=timeout)
        if result is None:
            logger.warning("Count query returned None, assuming 0 results")
            return 0

        return result if result is not None else 0
    except Exception as e:
        logger.warning(f"Could not estimate result size: {e}")
        return -1  # Unknown size


async def execute_query_with_fallback(
    sql_query: str, conn, timeout: int = QUERY_TIMEOUT
):
    """Execute query with automatic fallback strategies"""
    try:
        # Try original query first
        return await asyncio.wait_for(conn.fetch(sql_query), timeout=timeout)

    except asyncio.TimeoutError:
        logger.warning("Query timeout, attempting fallback with smaller limit")

        # Try with reduced limit
        if "limit" in sql_query.lower():
            fallback_query = re.sub(
                r"limit\s+\d+", "LIMIT 5", sql_query, flags=re.IGNORECASE
            )
        else:
            fallback_query = f"{sql_query.rstrip(';')} LIMIT 5"

        try:
            return await asyncio.wait_for(conn.fetch(fallback_query), timeout=10)
        except Exception as e:
            logger.error(f"Fallback query also failed: {e}")
            raise

    except Exception as e:
        logger.error(f"Query execution failed: {e}")
        raise


def validate_and_sanitize_sql(
    sql_query: str, count_mode: bool = False
) -> Tuple[bool, str, str]:
    """
    Validate and sanitize SQL query with enhanced security and structure checks

    Returns:
        (is_valid, sanitized_query, error_message)
    """
    sql_lower = sql_query.lower().strip()

    # Security checks - prevent dangerous operations
    dangerous_keywords = [
        "drop",
        "delete",
        "insert",
        "update",
        "alter",
        "create",
        "truncate",
        "exec",
    ]
    for keyword in dangerous_keywords:
        if f" {keyword} " in f" {sql_lower} " or sql_lower.startswith(keyword):
            return False, "", f"Dangerous SQL keyword '{keyword}' detected"

    # Structure validation
    if not sql_lower.startswith("select"):
        return False, "", "Only SELECT statements are allowed"

    # Check for required table reference
    if "eda_rag_data_augmented_e5.papers" not in sql_lower:
        return False, "", "Query must reference the papers table"

    # Add LIMIT if missing (unless it's a COUNT query)
    if not count_mode and "limit" not in sql_lower:
        sql_query = f"{sql_query.rstrip(';')} LIMIT {DEFAULT_LIMIT}"

    # Enforce maximum limit
    if "limit" in sql_lower and not count_mode:
        limit_match = re.search(r"limit\s+(\d+)", sql_lower)
        if limit_match:
            limit_value = int(limit_match.group(1))
            if limit_value > MAX_LIMIT:
                sql_query = re.sub(
                    r"limit\s+\d+", f"LIMIT {MAX_LIMIT}", sql_query, flags=re.IGNORECASE
                )
                logger.warning(f"Reduced LIMIT from {limit_value} to {MAX_LIMIT}")

    return True, sql_query, ""


class SQLQuery(BaseModel):
    sql: str


@tool
async def paper_database_tool(
    query: str,
    algorithm_names: Optional[List[str]] = None,
    paper_titles: Optional[List[str]] = None,
    author_surnames: Optional[List[str]] = None,
    paper_ids: Optional[List[int]] = None,
    year: Optional[str] = None,
    paper_url: Optional[str] = None,
    count: bool = False,
    data: bool = False,
    references: bool = False,
    limit: Optional[int] = None,
    offset: int = 0,
) -> str:
    """
    Enhanced academic paper database search with intelligent query processing.

    CRITICAL: The 'query' parameter is REQUIRED and must contain the original user's request/question.

    Args:
        query: REQUIRED - The original user's search query or instruction (e.g., "References of the paper X", "Papers by author Y", "Show me papers about Z")
        algorithm_names: Optional list of algorithm names to filter by
        paper_titles: Optional list of paper titles to filter by
        author_surnames: Optional list of author surnames to filter by
        paper_ids: Optional list of paper IDs to get specific papers and their URLs (useful for getting references from search results)
        year: Optional publication year to filter by
        paper_url: Optional paper URL to filter by
        count: Only if user is asking for a specific count of results (mutually exclusive with data)
        data: If True, return paper data or aggregated query results (mutually exclusive with count)
        references: Include references when a specific paper title/URL is provided
        limit: Maximum number of results to return (capped at MAX_LIMIT)
        offset: Number of results to skip (for pagination)

    Example usage:
        - Query: "References of the paper 'Title X'", references=True, paper_titles=["Title X"]
        - Query: "Papers by John Smith", author_surnames=["Smith"]
        - Query: "Show me UMDA papers", algorithm_names=["UMDA"]
    """

    # Validate mutually exclusive parameters
    if count and data:
        return "Error: 'count' and 'data' parameters are mutually exclusive"

    # Set default mode
    if not count and not data:
        data = True

    # Apply limit constraints
    if limit is None:
        limit = DEFAULT_LIMIT
    limit = min(limit, MAX_LIMIT)

    logger.info(
        "[paper_database_tool] Processing query='%s' algos=%s titles=%s authors=%s year=%s url=%s "
        "count=%s data=%s references=%s limit=%s offset=%s",
        query,
        algorithm_names,
        paper_titles,
        author_surnames,
        year,
        paper_url,
        count,
        data,
        references,
        limit,
        offset,
    )

    # Determine if references should be included
    include_refs = references and (
        paper_titles or paper_url or "reference" in query.lower()
    )

    # Normalize author surnames if provided
    if author_surnames:
        author_surnames = [unidecode(surname.lower()) for surname in author_surnames]

    try:
        # Enhance parameters for better SQL generation
        enhanced_params = enhance_sql_generation_parameters(
            query=query,
            algorithm_names=algorithm_names,
            paper_titles=paper_titles,
            author_surnames=author_surnames,
            paper_ids=paper_ids,
            year=year,
            paper_url=paper_url,
            return_count_only=count,
            data=data,
            references=include_refs,
            limit=limit,
            offset=offset,
            requested_limit=limit,  # Use limit as requested limit
            comprehensive_search=False,  # Default to false, can be set by LLM
            prioritize_recent=False,  # Default to false, can be set by LLM
        )

        # Generate SQL using LLM
        llm_prompt = SQL_GENERATION_PROMPT.format(**enhanced_params)

        from langchain_google_genai import ChatGoogleGenerativeAI

        llm = ChatGoogleGenerativeAI(
            model=LLM_CONFIG_GOOGLE["model"],
            temperature=LLM_CONFIG_GOOGLE["temperature"],
        )

        structured_sql_llm = llm.with_structured_output(SQLQuery)
        response = await structured_sql_llm.ainvoke(llm_prompt)

        # Extract SQL query from response
        if isinstance(response, SQLQuery):
            sql_query = response.sql.strip()
            raw_generated_sql = sql_query  # Save the raw generated SQL
        else:
            logger.error(
                f"[paper_database_tool] Unexpected response format: {response}"
            )
            return "Error: Unexpected response format from LLM"

        # Log the raw generated SQL for debugging
        logger.info(f"[paper_database_tool] Raw generated SQL from LLM: {sql_query}")
        print(f"DEBUG - Raw SQL from LLM: {sql_query}")  # Also print to console

        # Validate and sanitize SQL
        is_valid, sanitized_sql, error_msg = validate_and_sanitize_sql(sql_query, count)
        if not is_valid:
            logger.error(f"[paper_database_tool] SQL validation failed: {error_msg}")
            return f"Error: {error_msg}"

        sql_query = sanitized_sql

        # Log the final SQL query before execution for debugging
        logger.info(f"[paper_database_tool] Final SQL query to execute: {sql_query}")
        print(
            f"DEBUG - SQL Query: {sql_query}"
        )  # Also print to console for immediate visibility

        # Execute query with connection pool
        pool = await get_pg_pool()
        async with pool.acquire() as conn:
            # For data queries, estimate result size first
            estimated_size = -1
            if data and not count:
                estimated_size = await estimate_result_size(sql_query, conn)

                if estimated_size > 50:
                    logger.info(
                        f"[paper_database_tool] Large result set estimated: {estimated_size} rows"
                    )
                    # You could add user confirmation logic here if needed

            # Execute main query with fallback
            result = await execute_query_with_fallback(sql_query, conn)

        # Save raw results before processing
        raw_results = result

        # Process and format results
        if count:
            result_str = result
        else:
            result_str = format_results_intelligently(
                result, bool(include_refs), estimated_size
            )

        # Convert results to CSV format for comparison
        csv_results = (
            await convert_results_to_csv_with_headers(raw_results, sql_query, conn)
            if raw_results
            else None
        )

        # Prepare data for JSON logging
        log_entry = {
            "initial_query": query,
            "parameters": {
                "algorithm_names": algorithm_names,
                "paper_titles": paper_titles,
                "author_surnames": author_surnames,
                "year": year,
                "paper_url": paper_url,
                "count": count,
                "data": data,
                "references": references,  # Use the original parameter, not the computed include_refs
                "limit": limit,
                "offset": offset,
            },
            "computed_include_refs": include_refs,  # Log the computed value separately for debugging
            "raw_generated_sql": raw_generated_sql,
            "final_sql_query": sql_query,
            "raw_results": [
                list(row) if hasattr(row, "__iter__") else row for row in raw_results
            ]
            if raw_results
            else [],
            "raw_results_count": len(raw_results) if raw_results else 0,
            "csv_results": csv_results,
            "formatted_result": result_str,
            "estimated_size": estimated_size,
            "success": True,
        }

        # Save to JSON file
        await save_query_log(log_entry)

        logger.info(
            f"[paper_database_tool] Successfully processed query, returned {len(result) if result else 0} results"
        )
        return result_str

    except asyncio.TimeoutError:
        error_msg = (
            "Query timeout: The search took too long. Try a more specific query."
        )
        logger.error(f"[paper_database_tool] {error_msg}")

        # Log error case
        error_log_entry = {
            "initial_query": query,
            "error": error_msg,
            "error_type": "TimeoutError",
            "success": False,
        }
        await save_query_log(error_log_entry)

        return error_msg

    except Exception as e:
        error_msg = f"An error occurred while processing your request: {str(e)}"
        logger.error(f"[paper_database_tool] General error: {e}", exc_info=True)

        # Log error case
        error_log_entry = {
            "initial_query": query,
            "error": error_msg,
            "error_type": str(type(e).__name__),
            "success": False,
        }
        await save_query_log(error_log_entry)

        return error_msg


async def save_query_log(log_entry):
    """
    Save query log entry to JSON file.
    Appends to existing file or creates new one if it doesn't exist.
    """
    try:
        log_file_path = Path("paper_database_queries.json")

        # Load existing data if file exists
        if log_file_path.exists():
            with open(log_file_path, "r", encoding="utf-8") as f:
                try:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = []
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        # Append new entry
        existing_data.append(log_entry)

        # Save back to file
        with open(log_file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False, default=str)

        logger.info(f"[paper_database_tool] Query log saved to {log_file_path}")

    except Exception as e:
        logger.error(f"[paper_database_tool] Failed to save query log: {e}")


async def convert_results_to_csv_with_headers(raw_results, sql_query, conn):
    """
    Convert database results to CSV format with proper headers.
    Returns a string in CSV format suitable for comparison.
    """
    if not raw_results:
        return None

    try:
        # Try to get column names from the query
        column_names = await get_column_names_from_query(sql_query, conn)

        # Fallback: generate generic column names based on result structure
        if not column_names and raw_results:
            column_names = [f"col_{i + 1}" for i in range(len(raw_results[0]))]

        # Create CSV content
        csv_lines = []

        # Add header row
        if column_names:
            csv_lines.append(",".join(f'"{col}"' for col in column_names))

        # Add data rows
        for row in raw_results:
            csv_row = []
            for item in row:
                if item is None:
                    csv_row.append("")
                elif isinstance(item, str):
                    # Escape quotes and wrap in quotes if contains comma, quote, or newline
                    if "," in item or '"' in item or "\n" in item:
                        escaped_item = item.replace('"', '""')
                        csv_row.append(f'"{escaped_item}"')
                    else:
                        csv_row.append(item)
                elif isinstance(item, (int, float)):
                    csv_row.append(str(item))
                elif hasattr(item, "isoformat"):  # datetime objects
                    csv_row.append(item.isoformat())
                else:
                    csv_row.append(str(item))

            csv_lines.append(",".join(csv_row))

        return "\n".join(csv_lines)

    except Exception as e:
        logger.error(f"[paper_database_tool] Failed to convert results to CSV: {e}")
        return None


async def convert_results_to_csv(raw_results, conn):
    """
    Convert database results to CSV format for comparison purposes.
    Returns a string in CSV format with headers and data rows.
    """
    if not raw_results:
        return None

    try:
        # Get column names from the connection's last query description
        # This is a simplified approach - you might need to adjust based on your DB driver
        column_names = []
        if hasattr(conn, "description") and conn.description:
            column_names = [desc[0] for desc in conn.description]
        else:
            # Fallback: generate generic column names
            if raw_results:
                column_names = [f"col_{i + 1}" for i in range(len(raw_results[0]))]

        # Create CSV content
        csv_lines = []

        # Add header row
        if column_names:
            csv_lines.append(",".join(f'"{col}"' for col in column_names))

        # Add data rows
        for row in raw_results:
            csv_row = []
            for item in row:
                if item is None:
                    csv_row.append('""')
                elif isinstance(item, str):
                    # Escape quotes and wrap in quotes
                    escaped_item = item.replace('"', '""')
                    csv_row.append(f'"{escaped_item}"')
                elif isinstance(item, (int, float)):
                    csv_row.append(str(item))
                elif hasattr(item, "isoformat"):  # datetime objects
                    csv_row.append(f'"{item.isoformat()}"')
                else:
                    csv_row.append(f'"{str(item)}"')

            csv_lines.append(",".join(csv_row))

        return "\n".join(csv_lines)

    except Exception as e:
        logger.error(f"[paper_database_tool] Failed to convert results to CSV: {e}")
        return None


async def get_column_names_from_query(sql_query, conn):
    """
    Get column names by executing a LIMIT 0 version of the query.
    This helps us get proper column names for CSV headers.
    """
    try:
        # Create a version of the query that returns no rows but preserves structure
        if "limit" in sql_query.lower():
            # Replace existing limit with LIMIT 0
            import re

            modified_query = re.sub(
                r"\bLIMIT\s+\d+\b", "LIMIT 0", sql_query, flags=re.IGNORECASE
            )
        else:
            # Add LIMIT 0
            modified_query = f"{sql_query} LIMIT 0"

        # Execute to get column info
        result = await conn.fetch(modified_query)

        # Get column names from the result's keys (if available)
        if result and hasattr(result, "keys"):
            return list(result.keys())
        elif hasattr(conn, "_last_query_columns"):
            return conn._last_query_columns
        else:
            return None

    except Exception as e:
        logger.debug(f"[paper_database_tool] Could not get column names: {e}")
        return None


def convert_result_to_serializable(result):
    """
    Convert database result to JSON serializable format.
    Handles various data types that might not be JSON serializable.
    """
    if result is None:
        return None

    serializable_result = []
    for row in result:
        serializable_row = []
        for item in row:
            if item is None:
                serializable_row.append(None)
            elif isinstance(item, (str, int, float, bool)):
                serializable_row.append(item)
            elif hasattr(item, "isoformat"):  # datetime objects
                serializable_row.append(item.isoformat())
            else:
                serializable_row.append(str(item))
        serializable_result.append(serializable_row)

    return serializable_result


# List of all tools (basic tools without LLM access)
tools = [
    hybrid_search_tool,
    web_search_tool,
    paper_database_tool,
]


# def create_tools_with_llm(llm):
#     """
#     Factory function that creates tools with the LLM instance captured in closure.
#     This ensures the LLM is available to tools that need it without parameter passing.
#     """

#     # Context window protection constants
#     MAX_PAPERS_FOR_ALL = 50  # Maximum papers to return for "all" requests
#     FALLBACK_LIMIT = 10  # Fallback limit if "all" would be too many

#     # class SQLQuery(BaseModel):
#     #     sql: str

#     # structured_sql_llm = llm.with_structured_output(SQLQuery)

#     # Return the tools with LLM captured

#     return [
#         hybrid_search_tool,
#         paper_database_tool,
#         web_search_tool,
#     ]

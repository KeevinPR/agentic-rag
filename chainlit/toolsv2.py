"""
Enhanced Search and Utility Tools v2.0 for the EDA Research Assistant.

Major Enhancements:
- HyDE (Hypothetical Document Embeddings) for better semantic matching
- Abstract-first search strategy for scientific papers
- Dynamic weight adjustment based on query type
- Domain-specific boosting for EDA content
- Multi-strategy result fusion with intelligent fallbacks
- Query-aware re-ranking with type-specific thresholds
- Enhanced scientific paper optimizations
"""

import logging
import json
from pathlib import Path
import re
import textwrap
from typing import List, Optional, Dict, Any, Tuple
from unidecode import unidecode

from langchain_core.tools import tool
from langchain_tavily import TavilySearch
import asyncio
from config import SEARCH_CONFIG
from utils import (
    init_vector_stores,
    get_pg_pool,
)
from prompts import (
    SQL_GENERATION_PROMPT,
)
from sentence_transformers import CrossEncoder
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# Initialize the cross-encoder model once
cross_encoder = CrossEncoder(SEARCH_CONFIG["cross_encoder"]["model_name"])

# Constants for web search formatting
WRAP_WIDTH = 1000
DEFAULT_LIMIT = 10
MAX_LIMIT = 50
QUERY_TIMEOUT = 30

# Enhanced Scientific Search Configuration
ENHANCED_SEARCH_CONFIG = {
    "hyde": {
        "enabled": True,
        "docs_count": 3,
        "weight": 0.6,
        "temperature": 0.1,
        "max_tokens": 1024,
    },
    "abstract_first": {
        "enabled": True,
        "abstract_boost": 1.5,
        "abstract_weight": 0.7,
        "content_weight": 0.3,
    },
    "dynamic_weights": {
        "enabled": True,
        "base_semantic": 0.8,
        "base_fts": 0.2,
        "query_type_adjustments": {
            "formula": {"semantic": 0.6, "fts": 0.4},
            "algorithm": {"semantic": 0.7, "fts": 0.3},
            "concept": {"semantic": 0.9, "fts": 0.1},
            "paper_specific": {"semantic": 0.8, "fts": 0.2},
        },
        "rerank_thresholds": {
            "formula": 0.3,
            "algorithm": 0.4,
            "concept": 0.5,
            "paper_specific": 0.6,
        },
    },
    # "domain_boost": {
    #     "enabled": True,
    #     "eda_terms": [
    #         "estimation",
    #         "distribution",
    #         "algorithm",
    #         "probabilistic",
    #         "model",
    #         "optimization",
    #         "evolutionary",
    #         "genetic",
    #         "bayesian",
    #         "multivariate",
    #         "univariate",
    #         "gaussian",
    #         "copula",
    #         "marginal",
    #         "dependency",
    #     ],
    #     "boost_factor": 1.3,
    #     "citation_boost": 1.2,
    #     "recency_boost": 1.1,
    # },
    "multi_strategy": {
        "enabled": True,
        "semantic_candidates": 25,
        "fts_candidates": 15,
        "rerank_candidates": 20,
        "final_results": 5,
        "diversity_threshold": 0.85,
    },
}

print("✅ Enhanced Search Tools v2.0 configuration loaded!")


@tool
async def enhanced_hybrid_search_tool(
    raw_user_query: str,
    llm_query: str,
    paper_title: Optional[str] = None,
    algorithm_names: Optional[List[str]] = None,
    is_latex_query: Optional[bool] = False,
) -> str:
    """
    🚀 Next-generation hybrid search with advanced scientific paper optimizations.

    Revolutionary Features:
    ✨ HyDE (Hypothetical Document Embeddings) - Generates academic paper excerpts for better matching
    🎯 Abstract-First Strategy - Prioritizes abstracts for precision, expands to content for recall
    ⚖️ Dynamic Weight Adjustment - Adapts semantic/lexical balance based on query type
    🔬 Domain-Specific Boosting - EDA-aware content relevance scoring
    🧠 Query-Aware Re-ranking - Type-specific relevance thresholds
    🔄 Multi-Strategy Fusion - Combines multiple search approaches intelligently

    Args:
        raw_user_query: Original user question for natural language processing
        llm_query: LLM-processed search keywords/concepts
        paper_title: Optional paper filter for focused search
        algorithm_names: Specific algorithm names detected in query
        is_latex_query: Whether query seeks mathematical formulas/equations

    Returns:
        Enhanced search results with detailed relevance scoring
    """
    try:
        logger.info("🚀 Starting Enhanced Hybrid Search v2.0")
        logger.info(f"📝 Raw Query: {raw_user_query}")
        logger.info(f"🧠 Processed Query: {llm_query}")

        # Initialize search components
        vector_store = init_vector_stores()
        pool = await get_pg_pool()

        # Initialize LLM for HyDE generation
        from langchain_nvidia_ai_endpoints import ChatNVIDIA

        llm = ChatNVIDIA(
            model="meta/llama-3.3-70b-instruct",
            temperature=ENHANCED_SEARCH_CONFIG["hyde"]["temperature"],
            max_tokens=ENHANCED_SEARCH_CONFIG["hyde"]["max_tokens"],
        )

        # Step 1: Set fixed weights (dynamic classification removed for robustness)
        semantic_weight, fts_weight = 0.8, 0.2
        logger.info(
            f"⚖️ Using fixed weights: Semantic={semantic_weight:.2f}, FTS={fts_weight:.2f}"
        )

        # Step 2: HyDE Document Generation (Sequential before parallel tasks)
        hyde_docs = []
        if ENHANCED_SEARCH_CONFIG["hyde"]["enabled"] and not is_latex_query:
            hyde_docs = await _generate_hyde_documents(llm_query, llm)
            logger.info(f"📄 Generated {len(hyde_docs)} HyDE documents")
        elif is_latex_query:
            logger.info("📄 Skipping HyDE generation for LaTeX query.")

        # Step 3 & 4: Run Semantic and FTS searches in parallel
        logger.info("🚀 Launching Semantic and FTS searches in parallel...")

        semantic_task = _perform_multi_strategy_semantic_search(
            vector_store, llm_query, hyde_docs, paper_title
        )

        fts_task = _perform_enhanced_fts_search(
            pool,
            raw_user_query,
            llm_query,
            algorithm_names,
            is_latex_query,
            paper_title,
        )

        # Await both tasks to complete concurrently
        search_results = await asyncio.gather(semantic_task, fts_task)
        all_embedding_docs, all_fts_rows = search_results[0], search_results[1]

        logger.info(
            f"🔍 Retrieved in parallel: {len(all_embedding_docs)} semantic + {len(all_fts_rows)} FTS results"
        )

        # Step 5: Advanced RRF Fusion with Dynamic Weights
        rrf_scores = _calculate_enhanced_rrf(
            all_embedding_docs, all_fts_rows, semantic_weight, fts_weight
        )

        # Step 6: Candidate Selection for Re-ranking
        rerank_candidates = ENHANCED_SEARCH_CONFIG["multi_strategy"][
            "rerank_candidates"
        ]
        top_candidates = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[
            :rerank_candidates
        ]

        # Step 7: Prepare Candidate Documents
        candidate_docs = await _prepare_enhanced_candidate_docs(
            top_candidates, all_embedding_docs, all_fts_rows
        )

        # Step 8: Query-Aware Cross-Encoder Re-ranking
        rerank_query = raw_user_query if raw_user_query else llm_query
        if len(candidate_docs) >= 5:
            candidate_docs = await _perform_query_aware_reranking(
                rerank_query, candidate_docs
            )

        # Step 9: Domain-Specific Content Boosting (REMOVED)
        # candidate_docs = _apply_enhanced_domain_boosting(candidate_docs, llm_query)

        # Step 10: Result Diversification and Final Selection
        final_results = _select_diverse_results(
            candidate_docs, ENHANCED_SEARCH_CONFIG["multi_strategy"]["final_results"]
        )

        # Step 11: Enhanced Result Processing
        processed_results = await _process_enhanced_results(final_results)

        # Step 12: Generate Comprehensive Output
        output = _generate_enhanced_output(
            processed_results, len(all_embedding_docs), len(all_fts_rows)
        )

        # Step 13: Log Enhanced Search Metadata
        _log_enhanced_search_metadata(llm_query, top_candidates, final_results)

        return output

    except Exception as e:
        logger.error(f"❌ Enhanced search failed: {str(e)}", exc_info=True)
        # Graceful fallback to original search
        return await _fallback_to_original_search(
            raw_user_query, llm_query, paper_title, algorithm_names, is_latex_query
        )


async def _generate_hyde_documents(query: str, llm) -> List[str]:
    """📄 Generate hypothetical academic paper excerpts for enhanced semantic matching."""

    hyde_prompt = f"""You are an expert in Estimation of Distribution Algorithms (EDAs) research. Generate 3 different hypothetical academic paper excerpts that would perfectly answer this query. Each excerpt should be 2-3 sentences in formal academic style.

Query: {query}

Generate excerpts from these perspectives:
1. SURVEY_EXCERPT: An introductory/survey paper perspective
2. TECHNICAL_EXCERPT: A technical implementation/methodology paper  
3. COMPARATIVE_EXCERPT: A comparative analysis/experimental paper

Each excerpt should:
- Use academic terminology and style
- Be specific and technical when appropriate
- Represent how real papers would discuss this topic
- Include domain-specific EDA concepts when relevant

Format your response exactly as:
SURVEY_EXCERPT: [your excerpt here]
TECHNICAL_EXCERPT: [your excerpt here]  
COMPARATIVE_EXCERPT: [your excerpt here]"""

    try:
        response = await llm.ainvoke(hyde_prompt)
        excerpts = []

        # Parse structured response
        for line in response.content.split("\n"):
            if any(
                line.startswith(prefix)
                for prefix in [
                    "SURVEY_EXCERPT:",
                    "TECHNICAL_EXCERPT:",
                    "COMPARATIVE_EXCERPT:",
                ]
            ):
                if ": " in line:
                    excerpt = line.split(": ", 1)[1].strip()
                    if excerpt:  # Only add non-empty excerpts
                        excerpts.append(excerpt)

        logger.info(f"📄 HyDE generated {len(excerpts)} quality excerpts")
        logger.info("--- Generated HyDE Documents ---")
        for i, excerpt in enumerate(excerpts):
            logger.info(f"HyDE Excerpt {i + 1}: {excerpt}")
        logger.info("-----------------------------")
        return excerpts[:3]  # Ensure maximum 3 excerpts

    except Exception as e:
        logger.error(f"📄 HyDE generation failed: {e}")
        return []


async def _perform_multi_strategy_semantic_search(
    vector_store, query: str, hyde_docs: List[str], paper_title: Optional[str]
) -> Dict:
    """🔍 Multi-strategy semantic search with paper-guided chunk discovery."""

    filter_dict = {}
    paper_id = None

    # If paper_title provided, first get its paper_id
    if paper_title:
        pool = await get_pg_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                """
                SELECT paper_id 
                FROM eda_rag_data_simple.papers 
                WHERE title = $1
                LIMIT 1
                """,
                paper_title,
            )
            if row:
                paper_id = row["paper_id"]
                filter_dict["paper_id"] = paper_id
            else:
                logger.warning(f"Paper title not found: {paper_title}")

    all_results = {}
    candidates = ENHANCED_SEARCH_CONFIG["multi_strategy"]["semantic_candidates"]

    # Strategy 1: Abstract-First Paper Discovery (High Precision)
    discovered_papers = []
    if ENHANCED_SEARCH_CONFIG["abstract_first"]["enabled"] and not paper_id:
        # Find relevant papers via abstract search
        relevant_papers = await _discover_papers_via_abstracts(query, candidates // 3)
        discovered_papers.extend(relevant_papers)

        # Now search chunks within those discovered papers
        if discovered_papers:
            paper_guided_results = await _search_chunks_in_discovered_papers(
                vector_store, query, discovered_papers, candidates // 2
            )
            _merge_semantic_results(all_results, paper_guided_results, boost_factor=1.5)
            logger.info(
                f"📄 Paper-guided search: {len(paper_guided_results)} chunk results from {len(discovered_papers)} papers"
            )

    # Strategy 2: Full Content Semantic Search (High Recall)
    content_results = await _search_full_content(
        vector_store, query, candidates, filter_dict
    )
    _merge_semantic_results(all_results, content_results, boost_factor=1.0)

    # Strategy 3: HyDE-Enhanced Search (Vocabulary Gap Bridging)
    hyde_weight = ENHANCED_SEARCH_CONFIG["hyde"]["weight"]
    for hyde_doc in hyde_docs:
        hyde_results = await _search_full_content(
            vector_store, hyde_doc, candidates // 2, filter_dict
        )
        _merge_semantic_results(all_results, hyde_results, boost_factor=hyde_weight)

    logger.info(
        f"🔍 Multi-strategy semantic search: {len(all_results)} unique chunk results"
    )
    return all_results


async def _discover_papers_via_abstracts(query: str, k: int) -> List[Dict]:
    """📄 Discover relevant papers via abstract semantic search."""
    try:
        # Get embedding function from vector store
        vector_store = init_vector_stores()
        embedding_function = vector_store.embeddings

        # Generate query embedding
        query_embedding = await asyncio.to_thread(
            embedding_function.embed_query, f"query: {query}"
        )

        # Get database pool
        pool = await get_pg_pool()

        # Direct pgvector query on papers table
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT 
                    paper_id,
                    title,
                    authors, 
                    abstract,
                    paper_link,
                    year,
                    abstract_embedding <=> $1 AS distance
                FROM eda_rag_data_simple.papers
                WHERE abstract_embedding IS NOT NULL
                  AND abstract IS NOT NULL AND abstract != ''
                ORDER BY distance
                LIMIT $2;
            """,
                str(query_embedding),
                k,
            )

            # Convert to paper info dictionaries
            papers = []
            for row in rows:
                distance = row.get("distance")
                if distance is not None:
                    papers.append(
                        {
                            "paper_id": row["paper_id"],
                            "title": row["title"],
                            "authors": row["authors"],
                            "abstract": row["abstract"],
                            "distance": float(distance),
                            "similarity": 1.0 - float(distance),
                        }
                    )

            logger.info(f"📄 Abstract search discovered {len(papers)} relevant papers")
            return papers

    except Exception as e:
        logger.error(f"📄 Paper discovery failed: {e}")
        return []


async def _search_chunks_in_discovered_papers(
    vector_store, query: str, discovered_papers: List[Dict], k: int
) -> List:
    """📝 Search chunks within specific discovered papers."""
    try:
        all_paper_results = []

        # Get top papers by similarity (limit to avoid too many filters)
        top_papers = sorted(
            discovered_papers, key=lambda x: x["similarity"], reverse=True
        )[:8]

        for paper in top_papers:
            paper_id = paper["paper_id"]
            paper_filter = {"paper_id": paper_id}  # Use paper_id instead of title

            # Search chunks within this specific paper
            paper_results = vector_store.similarity_search_with_score(
                f"query: {query}", k=k // len(top_papers) + 1, filter=paper_filter
            )

            # Boost results based on abstract similarity
            abstract_boost = 1.0 + (paper["similarity"] * 0.5)  # Up to 1.5x boost

            for doc, score in paper_results:
                # Add paper discovery metadata
                doc.metadata["discovered_via_abstract"] = True
                doc.metadata["abstract_similarity"] = paper["similarity"]
                doc.metadata["discovery_boost"] = abstract_boost
                doc.metadata["source_paper_id"] = paper_id  # Add source paper_id

                boosted_score = score * abstract_boost
                all_paper_results.append((doc, boosted_score))

        # Sort by boosted score and return top results
        all_paper_results.sort(key=lambda x: x[1], reverse=True)
        return all_paper_results[:k]

    except Exception as e:
        logger.error(f"📝 Paper-guided chunk search failed: {e}")
        return []


async def _search_full_content(
    vector_store, query: str, k: int, filter_dict: Dict
) -> List:
    """📖 Search full content for broader recall."""
    try:
        return vector_store.similarity_search_with_score(
            f"query: {query}", k=k, filter=filter_dict
        )
    except Exception as e:
        logger.error(f"📖 Content search failed: {e}")
        return []


def _merge_semantic_results(all_results: Dict, new_results: List, boost_factor: float):
    """🔄 Merge semantic search results with optional boosting."""
    for doc, score in new_results:
        chunk_id = doc.metadata["chunk_id"]
        boosted_score = score * boost_factor

        if chunk_id not in all_results or boosted_score > all_results[chunk_id][1]:
            all_results[chunk_id] = (doc, boosted_score)


async def _perform_enhanced_fts_search(
    pool,
    raw_query: str,
    processed_query: str,
    algorithm_names: Optional[List[str]],
    is_latex_query: Optional[bool],
    paper_title: Optional[str],
) -> List:
    """🔎 Enhanced full-text search with intelligent query routing."""

    all_fts_rows = []
    fts_candidates = ENHANCED_SEARCH_CONFIG["multi_strategy"]["fts_candidates"]

    # Build filter conditions
    formula_filter = (
        "AND cmetadata->>'contains_formula' = 'true'" if is_latex_query else ""
    )
    paper_filter = ""
    if paper_title:
        escaped_title = paper_title.replace("'", "''")
        paper_filter = f"AND cmetadata->>'title' = '{escaped_title}'"

    # Strategy 1: Algorithm-specific search (if algorithms detected)
    if algorithm_names:
        await _fts_algorithm_search(
            pool,
            algorithm_names,
            formula_filter,
            paper_filter,
            fts_candidates,
            all_fts_rows,
        )

    # Strategy 2: Natural language search using raw query
    await _fts_natural_language_search(
        pool,
        raw_query,
        processed_query,
        formula_filter,
        paper_filter,
        fts_candidates,
        all_fts_rows,
    )

    return all_fts_rows


async def _fts_algorithm_search(
    pool,
    algorithm_names: List[str],
    formula_filter: str,
    paper_filter: str,
    limit: int,
    all_fts_rows: List,
):
    """🧬 Precise algorithm-focused FTS search."""
    try:
        # Filter out overly common terms
        filtered_names = [
            name
            for name in algorithm_names
            if len(name.strip()) >= 2 and name.lower() not in {"eda", "algorithm"}
        ]

        if not filtered_names:
            return

        # Create precise search terms
        search_terms = []
        for name in filtered_names:
            if " " in name:
                # Multi-word: use phrase search
                words = name.split()
                phrase = " <-> ".join(words)
                search_terms.append(f"({phrase})")
            else:
                # Single word: exact match with prefix option
                search_terms.append(f"{name}:*")

        fts_query = " | ".join(search_terms)
        logger.info(f"🧬 Algorithm FTS query: {fts_query}")

        async with pool.acquire() as conn:
            rows = await conn.fetch(
                f"""
                SELECT id, document, cmetadata,
                    ts_rank_cd(
                        to_tsvector('english', document),
                        to_tsquery('english', $1),
                        32
                    ) AS fts_score
                FROM eda_rag_data_augmented_e5.langchain_pg_embedding
                WHERE to_tsvector('english', document) @@ to_tsquery('english', $1)
                    {formula_filter}
                    {paper_filter}
                ORDER BY fts_score DESC
                LIMIT $2;
            """,
                fts_query,
                limit,
            )

            _merge_fts_results(rows, all_fts_rows)
            logger.info(f"🧬 Algorithm FTS: {len(rows)} results")

    except Exception as e:
        logger.warning(f"🧬 Algorithm FTS failed: {e}")


async def _fts_natural_language_search(
    pool,
    raw_query: str,
    processed_query: str,
    formula_filter: str,
    paper_filter: str,
    limit: int,
    all_fts_rows: List,
):
    """🗣️ Natural language FTS with intelligent fallbacks."""

    async with pool.acquire() as conn:
        # Primary: websearch_to_tsquery (best for natural language)
        if await _try_websearch_fts(
            conn, raw_query, formula_filter, paper_filter, limit, all_fts_rows
        ):
            return

        # Fallback: intelligent term extraction
        await _try_smart_term_search(
            conn, processed_query, formula_filter, paper_filter, limit, all_fts_rows
        )


async def _try_websearch_fts(
    conn,
    query: str,
    formula_filter: str,
    paper_filter: str,
    limit: int,
    all_fts_rows: List,
) -> bool:
    """🌐 Try websearch_to_tsquery for natural language processing."""
    try:
        rows = await conn.fetch(
            f"""
            SELECT id, document, cmetadata,
                ts_rank_cd(
                    to_tsvector('english', document),
                    websearch_to_tsquery('english', $1),
                    32
                ) AS fts_score
            FROM eda_rag_data_augmented_e5.langchain_pg_embedding
            WHERE to_tsvector('english', document) @@ websearch_to_tsquery('english', $1)
                {formula_filter}
                {paper_filter}
            ORDER BY fts_score DESC
            LIMIT $2;
        """,
            query,
            limit,
        )

        if rows:
            _merge_fts_results(rows, all_fts_rows)
            logger.info(f"🌐 Websearch FTS: {len(rows)} results")
            return True
        return False

    except Exception as e:
        logger.warning(f"🌐 Websearch FTS failed: {e}")
        return False


async def _try_smart_term_search(
    conn,
    processed_query: str,
    formula_filter: str,
    paper_filter: str,
    limit: int,
    all_fts_rows: List,
):
    """🧠 Smart term extraction and search."""
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
            "use",
            "used",
            "using",
            "paper",
            "study",
        }

        # Extract meaningful terms
        terms = []
        for word in re.findall(r"\b[a-zA-Z]+\b", processed_query.lower()):
            if len(word) >= 3 and word not in stop_words and not word.isdigit():
                terms.append(word)

        if len(terms) == 0:
            return

        # Create focused AND query for precision
        important_terms = terms[:4] if len(terms) > 4 else terms
        tsquery = " & ".join(important_terms)

        rows = await conn.fetch(
            f"""
            SELECT id, document, cmetadata,
                ts_rank_cd(
                    to_tsvector('english', document),
                    to_tsquery('english', $1),
                    32
                ) AS fts_score
            FROM eda_rag_data_augmented_e5.langchain_pg_embedding
            WHERE to_tsvector('english', document) @@ to_tsquery('english', $1)
                {formula_filter}
                {paper_filter}
            ORDER BY fts_score DESC
            LIMIT $2;
        """,
            tsquery,
            limit,
        )

        _merge_fts_results(rows, all_fts_rows)
        logger.info(f"🧠 Smart term FTS: {len(rows)} results")

    except Exception as e:
        logger.warning(f"🧠 Smart term search failed: {e}")


def _merge_fts_results(new_rows: List, all_fts_rows: List):
    """🔄 Merge FTS results avoiding duplicates."""
    existing_ids = {row["id"] for row in all_fts_rows}
    for row in new_rows:
        if row["id"] not in existing_ids:
            all_fts_rows.append(dict(row))
            existing_ids.add(row["id"])


def _calculate_enhanced_rrf(
    embedding_docs: Dict, fts_rows: List, semantic_weight: float, fts_weight: float
) -> Dict:
    """⚖️ Calculate RRF scores with dynamic weighting."""

    embedding_ranks = {
        chunk_id: idx for idx, (chunk_id, _) in enumerate(embedding_docs.items())
    }
    fts_ranks = {row["id"]: idx for idx, row in enumerate(fts_rows)}

    rrf_k = 1  # Standard RRF parameter
    all_chunk_ids = set(embedding_ranks.keys()) | set(fts_ranks.keys())
    rrf_scores = {}

    for chunk_id in all_chunk_ids:
        score = 0
        if chunk_id in embedding_ranks:
            score += semantic_weight / (rrf_k + embedding_ranks[chunk_id] + 1)
        if chunk_id in fts_ranks:
            score += fts_weight / (rrf_k + fts_ranks[chunk_id] + 1)
        rrf_scores[chunk_id] = score

    return rrf_scores


async def _prepare_enhanced_candidate_docs(
    top_candidates: List, embedding_docs: Dict, fts_rows: List
) -> List[Dict]:
    """📋 Prepare enhanced candidate documents with metadata."""

    candidate_docs = []

    for chunk_id, rrf_score in top_candidates:
        # Try to get from embedding results first
        if chunk_id in embedding_docs:
            doc, _ = embedding_docs[chunk_id]
            metadata_context = _extract_metadata_context(doc.metadata)

            candidate_docs.append(
                {
                    "id": chunk_id,
                    "content": doc.page_content,
                    "metadata_context": metadata_context,
                    "metadata": doc.metadata,
                    "score": rrf_score,
                    "source": "semantic",
                }
            )
        else:
            # Fallback to FTS results
            row = next((r for r in fts_rows if r["id"] == chunk_id), None)
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


def _extract_metadata_context(metadata: Dict) -> str:
    """📋 Extract useful context from metadata."""
    if not isinstance(metadata, dict):
        return ""

    context_parts = []
    if "source" in metadata:
        context_parts.append(f"Source: {metadata['source']}")
    if "title" in metadata:
        context_parts.append(f"Title: {metadata['title']}")
    if "authors" in metadata:
        context_parts.append(f"Authors: {metadata['authors']}")

    return "\n".join(context_parts) + ("\n" if context_parts else "")


def _parse_metadata(metadata) -> Dict:
    """📋 Parse metadata from various formats."""
    if isinstance(metadata, dict):
        return metadata
    elif isinstance(metadata, str):
        try:
            return json.loads(metadata)
        except json.JSONDecodeError:
            return {}
    else:
        return {}


async def _perform_query_aware_reranking(
    query: str, candidate_docs: List[Dict]
) -> List[Dict]:
    """🧠 Cross-encoder reranking with a fixed threshold for robustness."""

    threshold = 0.5  # Fixed threshold for simplicity and robustness

    try:
        # Prepare reranking pairs with enhanced context
        rerank_pairs = [
            (query, f"{doc['metadata_context']}{doc['content']}")
            for doc in candidate_docs
        ]

        # Get reranking scores with timeout
        rerank_scores = await asyncio.wait_for(
            asyncio.to_thread(cross_encoder.predict, rerank_pairs), timeout=30.0
        )

        # Apply scores and filter
        filtered_docs = []
        for i, doc in enumerate(candidate_docs):
            score = float(rerank_scores[i])
            doc["rerank_score"] = score

            if score >= threshold:
                filtered_docs.append(doc)

        if filtered_docs:
            result = sorted(
                filtered_docs, key=lambda x: x["rerank_score"], reverse=True
            )
            logger.info(
                f"🧠 Reranking: {len(result)}/{len(candidate_docs)} above threshold {threshold}"
            )
            return result
        else:
            # If no results above threshold, return all with scores
            logger.info(
                f"🧠 No results above threshold {threshold}, returning all with scores"
            )
            return sorted(
                candidate_docs, key=lambda x: x.get("rerank_score", 0), reverse=True
            )

    except Exception as e:
        logger.error(f"🧠 Reranking failed: {e}")
        return candidate_docs


def _select_diverse_results(candidate_docs: List[Dict], final_count: int) -> List[Dict]:
    """🎯 Select diverse, high-quality results to avoid redundancy."""

    if len(candidate_docs) <= final_count:
        return candidate_docs

    # Simple diversity selection based on content similarity
    selected = []
    diversity_threshold = ENHANCED_SEARCH_CONFIG["multi_strategy"][
        "diversity_threshold"
    ]

    for doc in candidate_docs:
        if len(selected) >= final_count:
            break

        # Check if this document is sufficiently different from already selected ones
        is_diverse = True
        for selected_doc in selected:
            # Simple overlap check (can be enhanced with embedding similarity)
            content1_words = set(doc["content"].lower().split())
            content2_words = set(selected_doc["content"].lower().split())

            if (
                len(content1_words & content2_words)
                / len(content1_words | content2_words)
                > diversity_threshold
            ):
                is_diverse = False
                break

        if is_diverse:
            selected.append(doc)

    # If we don't have enough diverse results, fill with highest scoring ones
    if len(selected) < final_count:
        remaining_docs = [doc for doc in candidate_docs if doc not in selected]
        selected.extend(remaining_docs[: final_count - len(selected)])

    return selected


async def _process_enhanced_results(results: List[Dict]) -> List[Dict]:
    """✨ Process results with enhanced formula handling and formatting."""

    processed_results = []

    for i, result in enumerate(results):
        try:
            # Enhanced formula processing
            await _process_formula_placeholders_enhanced([result])

            # Format content with enhanced styling
            formatted_content = f"**Chunk {i + 1}** (Score: {result.get('rerank_score', result.get('score', 0)):.3f})\n"

            # Add domain boost info if present
            # if "domain_boost" in result:
            #     formatted_content += (
            #         f"*Domain Relevance: {result['domain_boost']:.2f}x boost*\n"
            #     )

            formatted_content += f"{result['content']}\n"

            processed_results.append(
                {
                    "content": formatted_content,
                    "metadata": result["metadata"],
                    "score": result.get("rerank_score", result.get("score", 0.0)),
                    "source": result.get("source", "unknown"),
                    # "domain_boost": result.get("domain_boost"),
                    # "domain_matches": result.get("domain_matches", 0),
                }
            )

        except Exception as e:
            logger.warning(f"✨ Error processing result {i}: {e}")

    return processed_results


async def _process_formula_placeholders_enhanced(results: List[Dict]):
    """🧮 Enhanced formula placeholder processing."""

    for result in results:
        try:
            content = result["content"]
            metadata = _parse_metadata(result["metadata"])

            if not isinstance(metadata, dict) or "formulas" not in metadata:
                continue

            formulas = metadata["formulas"]
            if not isinstance(formulas, dict):
                continue

            # Create comprehensive placeholder mapping
            placeholder_mapping = {}
            for placeholder, formula in formulas.items():
                if isinstance(formula, str):
                    # Handle various placeholder formats
                    formats = _generate_placeholder_variants(placeholder)
                    for fmt in formats:
                        placeholder_mapping[fmt] = formula

            # Replace placeholders (longest first)
            if placeholder_mapping:
                content = _replace_placeholders_enhanced(content, placeholder_mapping)
                result["content"] = content

        except Exception as e:
            logger.warning(f"🧮 Formula processing error: {e}")


def _generate_placeholder_variants(placeholder: str) -> List[str]:
    """🧮 Generate placeholder format variants."""
    variants = [placeholder]

    if placeholder.startswith("[FORMULA_"):
        # Add version without underscore
        variants.append(placeholder.replace("_", ""))
    elif placeholder.startswith("[FORMULA") and "_" not in placeholder:
        # Add version with underscore
        variants.append(placeholder.replace("[FORMULA", "[FORMULA_"))

    return variants


def _replace_placeholders_enhanced(
    content: str, placeholder_mapping: Dict[str, str]
) -> str:
    """🧮 Enhanced placeholder replacement."""
    # Sort by length (longest first) to avoid partial replacements
    sorted_placeholders = sorted(placeholder_mapping.keys(), key=len, reverse=True)

    for placeholder in sorted_placeholders:
        if placeholder in content:
            formula = placeholder_mapping[placeholder]
            content = content.replace(placeholder, formula)

    return content


def _generate_enhanced_output(
    results: List[Dict], semantic_count: int, fts_count: int
) -> str:
    """📤 Generate comprehensive enhanced output as a JSON string for agent consumption."""

    if not results:
        return json.dumps(
            {
                "summary": "No relevant results found. Try refining your query.",
                "results": [],
            }
        )

    # Prepare a summary for the agent
    summary = f"""Enhanced Hybrid Search complete. 
- Candidates: {semantic_count} semantic + {fts_count} FTS.
- Final Results: {len(results)} matches after reranking and diversification."""

    # Clean results for final JSON output
    final_results_for_agent = []
    for res in results:
        metadata = res.get("metadata", {})
        if "formulas" in metadata:
            del metadata["formulas"]

        final_results_for_agent.append(
            {
                "content": res.get("content"),
                "metadata": metadata,
                "score": res.get("score"),
                "source": res.get("source"),
            }
        )

    output_data = {"summary": summary, "results": final_results_for_agent}

    return json.dumps(output_data, indent=2)


def _log_enhanced_search_metadata(
    query: str, top_candidates: List, final_results: List[Dict]
):
    """📊 Log enhanced search metadata for analysis."""

    metadata = {
        "query": query,
        "timestamp": json.dumps({"timestamp": "now"}, default=str),
        "candidate_count": len(top_candidates),
        "final_count": len(final_results),
        "enhancement_features": {
            "hyde_enabled": ENHANCED_SEARCH_CONFIG["hyde"]["enabled"],
            "abstract_first_enabled": ENHANCED_SEARCH_CONFIG["abstract_first"][
                "enabled"
            ],
            # "domain_boost_enabled": ENHANCED_SEARCH_CONFIG["domain_boost"]["enabled"],
        },
        "final_chunk_ids": [r.get("id") for r in final_results if r.get("id")],
        "candidate_chunk_ids": [cid for cid, _ in top_candidates],
    }

    # Save to enhanced search log
    _append_to_enhanced_search_log(metadata)


def _append_to_enhanced_search_log(metadata: Dict):
    """📊 Append to enhanced search log file."""

    log_file = Path("enhanced_search_log_v2.json")

    try:
        if log_file.exists():
            with open(log_file, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = []
        else:
            existing_data = []

        existing_data.append(metadata)

        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False, default=str)

        logger.info(f"📊 Enhanced search metadata logged to {log_file}")

    except Exception as e:
        logger.error(f"📊 Failed to log enhanced search metadata: {e}")


async def _fallback_to_original_search(
    raw_user_query: str,
    llm_query: str,
    paper_title: Optional[str],
    algorithm_names: Optional[List[str]],
    is_latex_query: Optional[bool],
) -> str:
    """🔄 Graceful fallback to original search implementation."""

    logger.info("🔄 Falling back to original search implementation")

    try:
        # Import and use original search logic
        from tools import hybrid_search_tool as original_search

        return await original_search.ainvoke(
            {
                "raw_user_query": raw_user_query,
                "llm_query": llm_query,
                "paper_title": paper_title,
                "algorithm_names": algorithm_names,
                "is_latex_query": is_latex_query,
            }
        )
    except Exception as e:
        logger.error(f"🔄 Fallback search also failed: {e}")
        return f"🚨 Search temporarily unavailable. Please try again. Error: {str(e)}"


# ===== WEB SEARCH TOOL (Enhanced) =====


@tool
async def enhanced_web_search_tool(query: str) -> str:
    """
    🌐 Enhanced web search with improved result formatting and analysis.

    Features:
    - Semantic result clustering
    - Enhanced relevance scoring
    - Academic source prioritization
    - Query term highlighting
    """
    try:
        logger.info("🌐 Processing enhanced web search: %s", query)

        tavily_search = TavilySearch(
            max_results=8,  # Increased for better coverage
            include_raw_content=True,
        )
        results = await tavily_search.ainvoke(query)

        if not results.get("results"):
            return "🔍 No web results found for your query."

        return _format_enhanced_web_results(results, query)

    except Exception as e:
        logger.error("🌐 Enhanced web search failed: %s", e, exc_info=True)
        return f"🚨 Web search failed: {e.__class__.__name__}"


def _format_enhanced_web_results(results: Dict, query: str) -> str:
    """🎨 Format web search results with enhanced styling."""

    out_lines = ["🌐 **Enhanced Web Search Results**\n"]

    # Add quick answer with enhanced formatting
    answer = results.get("answer")
    if answer:
        out_lines.append(f"💡 **Key Insight:** {answer}\n")

    # Enhanced query term highlighting
    terms = [re.escape(t.lower()) for t in query.split() if len(t) > 2]
    highlight_pattern = re.compile(r"\b(" + "|".join(terms) + r")\b", flags=re.I)

    # Process and rank results
    search_results = results["results"]

    # Prioritize academic/research sources
    def source_priority(result):
        url = result.get("url", "").lower()
        if any(
            domain in url
            for domain in ["scholar.google", "ieee", "acm.org", "arxiv", "researchgate"]
        ):
            return 0  # Highest priority
        elif any(domain in url for domain in ["edu", "gov"]):
            return 1  # High priority
        else:
            return 2  # Normal priority

    # Sort by source priority, then by score
    sorted_results = sorted(
        search_results, key=lambda x: (source_priority(x), -x.get("score", 0))
    )

    for idx, res in enumerate(sorted_results[:6], 1):  # Limit to top 6
        title = res.get("title", "No title")
        url = res.get("url", "No URL")
        content = res.get("content", "No content")
        score = res.get("score", 0)

        # Enhanced content processing
        content = " ".join(content.split())
        snippet = textwrap.shorten(content, width=WRAP_WIDTH, placeholder="…")

        # Apply highlighting
        title_highlighted = highlight_pattern.sub(r"**\1**", title)
        snippet_highlighted = highlight_pattern.sub(r"**\1**", snippet)

        # Academic source indicator
        source_indicator = (
            "🎓"
            if source_priority(res) == 0
            else "🏛️"
            if source_priority(res) == 1
            else "🔗"
        )

        out_lines.append(
            f"### {source_indicator} Result {idx} (Relevance: {score:.2f})\n"
            f"**{title_highlighted}**\n\n"
            f"{snippet_highlighted}\n\n"
            f"🔗 [{url}]({url})\n"
        )

    # Add search metadata
    response_time = results.get("response_time")
    if response_time:
        out_lines.append(f"\n⚡ *Search completed in {response_time:.2f} seconds*")

    return "\n".join(out_lines)


# ===== ENHANCED TOOLS LIST =====

enhanced_tools = [
    enhanced_hybrid_search_tool,
    enhanced_web_search_tool,
    # paper_database_tool,  # Import from original tools.py if needed
]


# ===== BACKWARDS COMPATIBILITY ALIASES =====

# For backwards compatibility, provide aliases to original tools
# hybrid_search_tool = enhanced_hybrid_search_tool
# web_search_tool = enhanced_web_search_tool

# # Main tools export
# tools = enhanced_tools

# if __name__ == "__main__":
#     # Test the enhanced search tool
#     import asyncio

#     async def test_enhanced_search():
#         result = await enhanced_hybrid_search_tool(
#             raw_user_query="What are the main types of estimation of distribution algorithms?",
#             llm_query="EDA types estimation distribution algorithms",
#             algorithm_names=["EDA"],
#             is_latex_query=False,
#         )
#         print(result)

#     # asyncio.run(test_enhanced_search())
#     print("✅ Enhanced Search Tools v2.0 loaded successfully!")

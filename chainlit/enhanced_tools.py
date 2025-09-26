#!/usr/bin/env python3
"""
Herramientas mejoradas que integran el ResponseImprover
para dar mejores respuestas contextuales sobre UMDA
"""

from langchain.tools import tool
from tools import hybrid_search_tool, paper_database_tool
from improved_response_handler import improve_umda_response
import asyncio

@tool
async def enhanced_hybrid_search_tool(
    raw_user_query: str,
    llm_query: str,
    paper_title: str = None,
    algorithm_names: list = None,
    is_latex_query: bool = False,
) -> str:
    """
    Versión mejorada del hybrid_search_tool que añade contexto y explicaciones
    especialmente para consultas sobre UMDA y otros algoritmos básicos.
    
    Args:
        raw_user_query: Consulta original del usuario
        llm_query: Consulta procesada por LLM
        paper_title: Título específico de paper (opcional)
        algorithm_names: Nombres de algoritmos mencionados
        is_latex_query: Si busca fórmulas LaTeX
    
    Returns:
        Respuesta mejorada con contexto y explicaciones
    """
    
    # Llamar a la herramienta original
    original_response = await hybrid_search_tool.ainvoke({
        "raw_user_query": raw_user_query,
        "llm_query": llm_query,
        "paper_title": paper_title,
        "algorithm_names": algorithm_names or [],
        "is_latex_query": is_latex_query
    })
    
    # Detectar si es consulta sobre UMDA
    if any(alg in ['UMDA', 'umda'] for alg in (algorithm_names or [])) or \
       'umda' in raw_user_query.lower():
        
        # Aplicar mejoras específicas para UMDA
        improved_response = improve_umda_response(raw_user_query, original_response)
        return improved_response
    
    # Para otros algoritmos, devolver respuesta original por ahora
    return original_response

@tool 
async def enhanced_paper_database_tool(
    query: str,
    algorithm_names: list = None,
    paper_titles: list = None,
    author_surnames: list = None,
    paper_ids: list = None,
    year: str = None,
    paper_url: str = None,
    count: bool = False,
    data: bool = False,
    references: bool = False,
    limit: int = None,
    offset: int = 0,
) -> str:
    """
    Versión mejorada del paper_database_tool que añade contexto sobre
    los tipos de papers encontrados.
    """
    
    # Llamar a la herramienta original
    original_response = await paper_database_tool.ainvoke({
        "query": query,
        "algorithm_names": algorithm_names,
        "paper_titles": paper_titles, 
        "author_surnames": author_surnames,
        "paper_ids": paper_ids,
        "year": year,
        "paper_url": paper_url,
        "count": count,
        "data": data,
        "references": references,
        "limit": limit,
        "offset": offset
    })
    
    # Añadir contexto si es sobre UMDA básico
    if 'umda' in query.lower() and any(keyword in query.lower() for keyword in ['básica', 'basic', 'fundamental']):
        context = """
⚠️ **NOTA:** Los papers encontrados pueden contener análisis teóricos avanzados. 
Si buscas la implementación básica de UMDA, la fórmula fundamental es:

$$p_i(t+1) = \\frac{1}{\\mu} \\sum_{j=1}^{\\mu} x_i^{(j)}$$

---

"""
        return context + original_response
    
    return original_response

# Función de prueba
async def test_enhanced_tools():
    """Probar las herramientas mejoradas"""
    
    print("🧪 Probando herramientas mejoradas...")
    
    # Prueba 1: Consulta básica sobre UMDA
    print("\n1️⃣ Consulta básica sobre UMDA:")
    response1 = await enhanced_hybrid_search_tool(
        raw_user_query="¿Cuál es la fórmula básica de UMDA?",
        llm_query="fórmula básica UMDA",
        algorithm_names=["UMDA"],
        is_latex_query=True
    )
    print("Respuesta (primeros 500 chars):")
    print(response1[:500] + "...")
    
    print("\n" + "="*60)
    
    # Prueba 2: Búsqueda de papers
    print("\n2️⃣ Búsqueda de papers básicos sobre UMDA:")
    response2 = await enhanced_paper_database_tool(
        query="papers básicos sobre UMDA",
        algorithm_names=["UMDA"],
        data=True,
        limit=3
    )
    print("Respuesta (primeros 300 chars):")
    print(response2[:300] + "...")

if __name__ == "__main__":
    asyncio.run(test_enhanced_tools())

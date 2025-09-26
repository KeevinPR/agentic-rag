"""
Simple in-memory caching system for AI responses to reduce latency for repeated queries.
"""

import hashlib
import time
import logging
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass
import unicodedata

logger = logging.getLogger(__name__)

@dataclass
class CacheEntry:
    """Cache entry with response and metadata"""
    response: str
    timestamp: float
    hit_count: int = 0

class ResponseCache:
    """Simple in-memory cache for AI responses"""
    
    def __init__(self, max_entries: int = 1000, ttl_seconds: int = 3600):  # 1 hour TTL
        self.cache: Dict[str, CacheEntry] = {}
        self.max_entries = max_entries
        self.ttl_seconds = ttl_seconds
        
    def _normalize_text(self, text: str) -> str:
        """Normalize text: lowercase, remove accents/diacritics, collapse spaces"""
        if not text:
            return ""
        # Lowercase
        text = text.lower().strip()
        # Remove accents/diacritics
        text = unicodedata.normalize('NFD', text)
        text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
        # Collapse whitespace
        text = ' '.join(text.split())
        return text

    def _hash_query(self, query: str) -> str:
        """Create a hash key for the query using normalized text"""
        normalized = self._normalize_text(query)
        return hashlib.md5(normalized.encode('utf-8')).hexdigest()
    
    def _is_expired(self, entry: CacheEntry) -> bool:
        """Check if cache entry is expired"""
        return (time.time() - entry.timestamp) > self.ttl_seconds
    
    def _cleanup_expired(self):
        """Remove expired entries"""
        current_time = time.time()
        expired_keys = [
            key for key, entry in self.cache.items() 
            if (current_time - entry.timestamp) > self.ttl_seconds
        ]
        
        for key in expired_keys:
            del self.cache[key]
            
        if expired_keys:
            logger.info(f"🧹 Cleaned up {len(expired_keys)} expired cache entries")
    
    def _evict_oldest(self):
        """Evict oldest entries if cache is full"""
        if len(self.cache) >= self.max_entries:
            # Sort by timestamp and remove oldest 10%
            sorted_entries = sorted(
                self.cache.items(), 
                key=lambda x: x[1].timestamp
            )
            
            num_to_remove = max(1, len(sorted_entries) // 10)
            for key, _ in sorted_entries[:num_to_remove]:
                del self.cache[key]
                
            logger.info(f"🧹 Evicted {num_to_remove} oldest cache entries")
    
    def get(self, query: str) -> Optional[str]:
        """Get cached response if available and not expired"""
        key = self._hash_query(query)
        
        if key not in self.cache:
            return None
            
        entry = self.cache[key]
        
        if self._is_expired(entry):
            del self.cache[key]
            return None
        
        # Update hit count and return response
        entry.hit_count += 1
        logger.info(f"✅ Cache HIT for query (hit #{entry.hit_count})")
        return entry.response
    
    def put(self, query: str, response: str):
        """Store response in cache"""
        # Clean up expired entries periodically
        if len(self.cache) % 100 == 0:  # Every 100 entries
            self._cleanup_expired()
        
        # Evict oldest if needed
        self._evict_oldest()
        
        key = self._hash_query(query)
        self.cache[key] = CacheEntry(
            response=response,
            timestamp=time.time()
        )
        
        logger.info(f"💾 Cached response for query (cache size: {len(self.cache)})")
    
    def clear(self):
        """Clear all cache entries"""
        self.cache.clear()
        logger.info("🧹 Cache cleared")
    
    def stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        current_time = time.time()
        expired_count = sum(
            1 for entry in self.cache.values() 
            if (current_time - entry.timestamp) > self.ttl_seconds
        )
        
        total_hits = sum(entry.hit_count for entry in self.cache.values())
        
        return {
            "total_entries": len(self.cache),
            "expired_entries": expired_count,
            "total_hits": total_hits,
            "max_entries": self.max_entries,
            "ttl_seconds": self.ttl_seconds
        }

# Global cache instance
_response_cache: Optional[ResponseCache] = None

def get_response_cache() -> ResponseCache:
    """Get or create the global response cache"""
    global _response_cache
    
    if _response_cache is None:
        # Claude 3.5 Sonnet v2 optimized cache settings
        _response_cache = ResponseCache(max_entries=1000, ttl_seconds=2700)  # 45 minutes, more entries
        logger.info("💾 Response cache initialized for Claude 3.5 Sonnet v2")
    
    return _response_cache

def clear_response_cache():
    """Clear the global response cache"""
    global _response_cache
    
    if _response_cache:
        _response_cache.clear()

def is_cacheable_query(query: str) -> bool:
    """Determine if a query should be cached"""
    # Cache simple definition queries and common questions
    cacheable_patterns_en = [
        "what is", "what are", "define", "explain",
        "how does", "how do", "pseudocode for",
        "algorithm for", "example of"
    ]
    # Spanish patterns (normalized without accents)
    cacheable_patterns_es = [
        "que es", "que son", "definicion de", "explica",
        "como funciona", "pseudocodigo de",
        "algoritmo de", "ejemplo de", "para que sirve"
    ]

    # Normalize query (lowercase, no accents, collapsed spaces)
    query_lower = query.lower().strip()
    query_lower = unicodedata.normalize('NFD', query_lower)
    query_lower = ''.join(ch for ch in query_lower if unicodedata.category(ch) != 'Mn')
    query_lower = ' '.join(query_lower.split())
    
    # Don't cache very long queries (likely complex/unique)
    if len(query) > 200:
        return False
    
    # Don't cache queries with time-sensitive words
    time_sensitive = [
        # English
        "recent", "latest", "new", "current", "today", "now",
        # Spanish (normalized, without accents)
        "reciente", "ultimo", "ultimos", "hoy", "ahora",
        # Years
        "2024", "2025"
    ]
    if any(word in query_lower for word in time_sensitive):
        return False
    
    # Cache if it matches common patterns
    return any(pattern in query_lower for pattern in cacheable_patterns_en + cacheable_patterns_es)

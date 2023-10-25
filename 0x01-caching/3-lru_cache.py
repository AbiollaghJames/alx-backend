#!/usr/bin/env python3
"""
LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        LRU Algorithm
        """
        if key and item:
            new_cache = {key: item}
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(lru_key)
                print(f"DISCARD: {lru_key}")
            self.cache_data.update(new_cache)

    def get(self, key):
        """
        Get item from cache_data dict by key
        """
        cache = self.cache_data.get(key)
        if cache:
            self.cache_data.pop(key)
            self.cache_data.update({key: cache})
        return cache

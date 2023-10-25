#!/usr/bin/env python3
"""
MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        MRU Algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Get item from cache_data dict by key
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item

        return self.cache_data[key]

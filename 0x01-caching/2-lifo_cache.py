#!/usr/bin/env python3
"""
LIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.keys_in_cache = []

    def put(self, key, item):
        """
        LIFO Algorithm
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.keys_in_cache.remove(key)
                else:
                    key_to_discard = self.keys_in_cache.pop()
                    del self.cache_data[key_to_discard]
                    print(f"DISCARD: {key_to_discard}")

        self.cache_data[key] = item
        self.keys_in_cache.append(key)

    def get(self, key):
        """
        Get item from cache_data dict by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

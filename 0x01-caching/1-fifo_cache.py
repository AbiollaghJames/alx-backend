#!/usr/bin/env python3
"""
FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.keys_in_cache = []

    def put(self, key, item):
        """
        FIFO Algorithm
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                key_to_discard = self.keys_in_cache.pop(0)
                del self.cache_data[key_to_discard]
                print(f"DISCARD: ", key_to_discard)

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

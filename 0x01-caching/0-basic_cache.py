#!/usr/bin/env python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from
    BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        Adds item to the cache_data dict
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item from cache_data dict by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

#!/usr/bin/env python3
"""
LFUCache module
"""

from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.usage_count = defaultdict(int)
        self.min_count = 1

    def put(self, key, item):
        """
        LFU Algorithm
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_key = min(self.usage_count, key=lambda k: self.usage_count[k])
                min_keys = [k for k in self.usage_count if self.usage_count[k] == self.usage_count[min_key]]
                min_key = min(min_keys, key=lambda k: self.usage_count[k])
                print(f"DISCARD: {min_key}")

                del self.cache_data[min_key]
                del self.usage_count[min_key]

            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.min_count = 1

    def get(self, key):
        """
        Get item from cache_data dict by key
        """
        if key in self.cache_data:
            self.usage_count[key] += 1
            return self.cache_data[key]
        else:
            return None

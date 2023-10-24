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
        super().__init__()
        self.keys_in_cache = []
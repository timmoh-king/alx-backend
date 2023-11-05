#!/usr/bin/env python3

"""
    Create a cls LIFOCache that inherits from BaseCaching as a caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache"""
    def __init__(self):
        """declare class constraints and variables"""
        super().__init__()

    def put(self, key, item):
        """
            assign to the dict self.cache_data the item value for the key key.
            If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.cache_data.popitem()
            print(f"DISCARD: {discarded[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)

#!/usr/bin/env python3

"""
    Create a cls FIFOCache that inherits from BaseCaching as a caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching

from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
        class FIFOCache
    """
    def __init__(self):
        """initialize the super class variables and constraints"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            assign to the dict self.cache_data the item value for the key key.
            If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.cache_data.popitem(False)
            print(f"DISCARD: {discarded[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
            If key is None or key not exist in self.cache_data, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)

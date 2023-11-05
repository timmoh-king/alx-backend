#!/usr/bin/env python3

"""
    Create a cls LIFOCache that inherits from BaseCaching as a caching system:
"""

from base_caching import BaseCaching

from collections import OrderedDict


class LIFOCache(BaseCaching):
    """class LIFOCache"""
    def __init__(self):
        """declare class constraints and variables"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            assign to the dict self.cache_data the item value for the key key.
            If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            discarded = self.cache_data.popitem(True)
            print(f"DISCARD: {discarded[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)

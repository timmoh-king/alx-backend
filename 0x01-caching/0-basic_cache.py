#!/usr/bin/env python3

"""
    Create a class BasicCache that inherits from BaseCaching as caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        class BasicCache
    """
    def __init__(self):
        """ initialize the super class variables and constraints"""
        super().__init__()

    def put(self, key, item):
        """
            assign cache_data the item value for the key
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
            return the value in cache_data linked to the key
        """
        return self.cache_data.get(key)

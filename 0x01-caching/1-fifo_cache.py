#!/usr/bin/env python3
"""First-In First Out caching module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    algorithm when the limit is reached
    """
    def __init__(self):
        """Initializes the cache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = list(self.cache_data)[0]
            print("DISCARD: {}".format(first_item))
            del self.cache_data[first_item]

    def get(self, key):
        """Retrieves an item by key"""
        return self.cache_data.get(key, None)

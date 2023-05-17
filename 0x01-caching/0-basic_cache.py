#!/usr/bin/python3
"""module docs for 0-basic_cache.py"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key=None, item=None):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            data = {key: item}
            return self.cache_data.update(data)
        else:
            return

    def get(self, key=None):
        """ Get an item by key
        """
        return self.cache_data.get(key)

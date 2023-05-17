#!/usr/bin/python3
"""module docs for 0-basic_cache.py"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Basic Cache class"""

    def __init__(self):  # method overloading
        self.orders = []  # list to keep track of items
        super().__init__()  # also inheriting Base class

    def put(self, key=None, item=None):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            data = {key: item}
            if self.MAX_ITEMS > len(self.orders):
                self.orders.append(key)
                self.cache_data.update(data)
                # print(self.orders)
            elif key in self.cache_data:
                self.cache_data.update(data)
            else:
                pop_it = self.orders.pop(0)
                # print(f"To be deleted {pop_it}")
                del self.cache_data[pop_it]
                self.orders.append(key)
                self.cache_data.update(data)
                print(f"DISCARD: {pop_it}", end="\n")
        else:
            return

    def get(self, key=None):
        """ Get an item by key
        """
        return self.cache_data.get(key)

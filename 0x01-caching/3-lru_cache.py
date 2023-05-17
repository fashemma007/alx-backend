#!/usr/bin/python3
"""module docs for 0-basic_cache.py"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used Cache class"""

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
                self._reorder(key)
            else:
                pop_it = self.orders.pop(0)
                # print(f"To be deleted {pop_it}")
                del self.cache_data[pop_it]
                self.cache_data.update(data)
                self._reorder(key)
                print(f"DISCARD: {pop_it}", end="\n")
        else:
            return

    def get(self, key=None):
        """ Get an item by key
        """
        self._reorder(key)
        return self.cache_data.get(key)

    def _reorder(self, key):
        """reoders keys in orders list"""
        # change the position of updated key in the `orders` list
        key_vals = self.cache_data.get(key)
        # print(f"key_vals: {key_vals}")
        try:
            [self.orders.remove(i) for i in self.orders if i == key]
        except ValueError:
            pass
        if key_vals is not None:
            self.orders.append(key)
        # print(self.orders)

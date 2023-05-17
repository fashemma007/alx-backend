#!/usr/bin/python3
"""module docs for 0-basic_cache.py"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LEast Frequently Used Cache class"""

    def __init__(self):  # method overloading
        self.orders = {}  # list to keep track of items
        super().__init__()  # also inheriting Base class

    def put(self, key=None, item=None):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            data = {key: item}
            if self.MAX_ITEMS > len(self.orders):
                self.cache_data.update(data)
                self._incr_key(key)
                # print(self.orders)
            elif key in self.cache_data:
                self.cache_data.update(data)
                self._incr_key(key)
            else:
                pop_it = min(self.orders, key=self.orders.get)
                # print(f"To be deleted {pop_it}")
                del self.orders[pop_it]  # delete in orders as well
                del self.cache_data[pop_it]
                self.cache_data.update(data)
                self._incr_key(key)
                print(f"DISCARD: {pop_it}", end="\n")
        else:
            return

    def get(self, key=None):
        """ Get an item by key
        """
        self._incr_key(key)
        return self.cache_data.get(key)

    def _incr_key(self, key):
        """increases key frequency"""
        # change the position of updated key in the `orders` list
        key_vals = self.orders.get(key)
        if key in self.cache_data:  # ensure data present before increasing
            if key_vals is None:  # avoid KeyError and create k,v pair
                self.orders[key] = 0
            else:  # increase value
                self.orders[key] += 1
        # print(self.orders)

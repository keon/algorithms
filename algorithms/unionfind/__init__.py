import pyreunion


class UnionFind:
    """A simple Proxy of pyreunion.UnionFind.
        
        Here we provide some extra utilities in the API
        like unionAll().

    """

    def __init__(self, *args, **kwargs):
        """ Proxy the UnionFind using a composition API.
        """

        self._unionfind = pyreunion.UnionFind(*args, **kwargs)

        # The pyreunion.UnionFind only supports int as its members for now.

        # One way to allow any hashable type is by storing a bidirectional mapping
        # to identify arbitrary hashable members with int values and vice versa.

        self._member_to_key = dict()
        self._key_to_member = dict()
    
    def __str__(self):
        return str(self._unionfind)

    __repr__ = __str__

    def unionAll(self, *args):
        """ Union the groups that the passed arguments are contained in.

        """
        if len(args) < 2:
            return

        for first, second in zip(args[:-1], args[1:]):
            self.union(first, second)
        return

    def __getitem__(self, item):
        """Treat getitem the same as find."""
        return self.find(item)
    
    def union(self, itemA, itemB):

        if itemA not in self._member_to_key:
            # Cache a new mapping.
            self._key_to_member[len(self._member_to_key)] = itemA
            self._member_to_key[itemA] = len(self._member_to_key)

        if itemB not in self._member_to_key:
            # Cache a new mapping.
            self._key_to_member[len(self._member_to_key)] = itemB
            self._member_to_key[itemB] = len(self._member_to_key)
        
        query_itemA_key = self._member_to_key[itemA]
        query_itemB_key = self._member_to_key[itemB]
        
        return self._unionfind.union(query_itemA_key, query_itemB_key)

    def find(self, item):
        if item not in self._member_to_key:
            # Cache a new mapping.
            self._key_to_member[len(self._member_to_key)] = item
            self._member_to_key[item] = len(self._member_to_key)

        query_key = self._member_to_key[item]
        parent_key = self._unionfind.find(query_key)
        parent = self._key_to_member[parent_key]

        return parent


import unittest


class Node(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class SeparateChainingHashTable(object):
    """
    HashTable Data Type:
    By having each bucket contain a linked list of elements that are hashed to that bucket.

    Usage:
    >>> table = SeparateChainingHashTable() # Create a new, empty map.
    >>> table.put('hello', 'world') # Add a new key-value pair.
    >>> len(table) # Return the number of key-value pairs stored in the map.
    1
    >>> table.get('hello') # Get value by key.
    'world'
    >>> del table['hello'] # Equivalent to `table.del_('hello')`, deleting key-value pair.
    >>> table.get('hello') is None # Return `None` if a key doesn't exist.
    True
    """
    _empty = None

    def __init__(self, size=11):
        self.size = size
        self._len = 0
        self._table = [self._empty] * size

    def put(self, key, value):
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        if node_ is self._empty:
            self._table[hash_] = Node(key, value)
        else:
            while node_.next is not None:
                if node_.key == key:
                    node_.value = value
                    return
                node_ = node_.next
            node_.next = Node(key, value)
        self._len += 1

    def get(self, key):
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        while node_ is not self._empty:
            if node_.key == key:
                return node_.value
            node_ = node_.next
        return None

    def del_(self, key):
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        pre_node = None
        while node_ is not None:
            if node_.key == key:
                if pre_node is None:
                    self._table[hash_] = node_.next
                else:
                    pre_node.next = node_.next
                self._len -= 1
            pre_node = node_
            node_ = node_.next

    def hash(self, key):
        return hash(key) % self.size

    def __len__(self):
        return self._len

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.del_(key)

    def __setitem__(self, key, value):
        self.put(key, value)

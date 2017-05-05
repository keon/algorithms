"""
MAP Abstract Data Type
Map() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored in the map.
in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
"""
from unittest import TestCase


class HashTable(object):
    def __init__(self, size=11):
        self.size = size
        self.keys = [None] * size  # keys
        self.values = [None] * size  # values

    def put(self, key, value):
        hash_value = self.hash(key)

        if hash_value not in keys:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        else:
            if self.keys[hash_value] == key:  # replace
                self.values[hash_value] = value
            else:  # probing
                rehashval = self.rehash(key)
                while self.keys[rehashval] is not None and \
                                self.keys[rehashval] != key:
                    rehashval = self.rehash(rehashval)
                if keys[rehashval] is None:
                    self.keys[rehashval] = key
                    self.values[rehashval] = value
                else:
                    self.values[rehashval] = value  # replacee

    def get(self, key):
        pass

    def hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        """
        linear probing
        """
        return (old_hash + 1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


class TestHashTable(TestCase):
    def test_one_entry(self):
        m = HashTable(10)
        m.put(1, '1')
        self.assertEqual('1', m.get(1))

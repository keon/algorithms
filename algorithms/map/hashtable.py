from unittest import TestCase
import unittest

class HashTable(object):
    """
    HashMap Data Type
    HashMap() Create a new, empty map. It returns an empty map collection.
    put(key, val) Add a new key-value pair to the map. If the key is already in the map then replace
                    the old value with the new value.
    get(key) Given a key, return the value stored in the map or None otherwise.
    del_(key) or del map[key] Delete the key-value pair from the map using a statement of the form del map[key].
    len() Return the number of key-value pairs stored in the map.
    in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
    """

    _empty = object()
    _deleted = object()

    def __init__(self, size=11):
        self.size = size
        self._len = 0
        self._keys = [self._empty] * size  # keys
        self._values = [self._empty] * size  # values

    def put(self, key, value):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty or self._keys[hash_] is self._deleted:
                # can assign to hash_ index
                self._keys[hash_] = key
                self._values[hash_] = value
                self._len += 1
                return
            elif self._keys[hash_] == key:
                # key already exists here, assign over
                self._keys[hash_] = key
                self._values[hash_] = value
                return

            hash_ = self._rehash(hash_)

            if initial_hash == hash_:
                # table is full
                raise ValueError("Table is full")

    def get(self, key):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                # That key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found
                return self._values[hash_]

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def del_(self, key):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                # That key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found, assign with deleted sentinel
                self._keys[hash_] = self._deleted
                self._values[hash_] = self._deleted
                self._len -= 1
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def hash(self, key):
        return key % self.size

    def _rehash(self, old_hash):
        """
        linear probing
        """
        return (old_hash + 1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.del_(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self._len


class ResizableHashTable(HashTable):
    MIN_SIZE = 8

    def __init__(self):
        super().__init__(self.MIN_SIZE)

    def put(self, key, value):
        rv = super().put(key, value)
        # increase size of dict * 2 if filled >= 2/3 size (like python dict)
        if len(self) >= (self.size * 2) / 3:
            self.__resize()

    def __resize(self):
        keys, values = self._keys, self._values
        self.size *= 2  # this will be the new size
        self._len = 0
        self._keys = [self._empty] * self.size
        self._values = [self._empty] * self.size
        for key, value in zip(keys, values):
            if key is not self._empty and key is not self._deleted:
                self.put(key, value)


class TestHashTable(TestCase):
    def test_one_entry(self):
        m = HashTable(10)
        m.put(1, '1')
        self.assertEqual('1', m.get(1))

    def test_add_entry_bigger_than_table_size(self):
        m = HashTable(10)
        m.put(11, '1')
        self.assertEqual('1', m.get(11))

    def test_get_none_if_key_missing_and_hash_collision(self):
        m = HashTable(10)
        m.put(1, '1')
        self.assertEqual(None, m.get(11))

    def test_two_entries_with_same_hash(self):
        m = HashTable(10)
        m.put(1, '1')
        m.put(11, '11')
        self.assertEqual('1', m.get(1))
        self.assertEqual('11', m.get(11))

    def test_get_on_full_table_does_halts(self):
        # and does not search forever
        m = HashTable(10)
        for i in range(10, 20):
            m.put(i, i)
        self.assertEqual(None, m.get(1))

    def test_delete_key(self):
        m = HashTable(10)
        for i in range(5):
            m.put(i, i**2)
        m.del_(1)
        self.assertEqual(None, m.get(1))
        self.assertEqual(4,m.get(2))

    def test_delete_key_and_reassign(self):
        m = HashTable(10)
        m.put(1, 1)
        del m[1]
        m.put(1, 2)
        self.assertEqual(2, m.get(1))

    def test_assigning_to_full_table_throws_error(self):
        m = HashTable(3)
        m.put(1, 1)
        m.put(2, 2)
        m.put(3, 3)
        with self.assertRaises(ValueError):
            m.put(4, 4)

    def test_len_trivial(self):
        m = HashTable(10)
        self.assertEqual(0, len(m))
        for i in range(10):
            m.put(i, i)
            self.assertEqual(i + 1, len(m))

    def test_len_after_deletions(self):
        m = HashTable(10)
        m.put(1, 1)
        self.assertEqual(1, len(m))
        m.del_(1)
        self.assertEqual(0, len(m))
        m.put(11, 42)
        self.assertEqual(1, len(m))

    def test_resizable_hash_table(self):
        m = ResizableHashTable()
        self.assertEqual(ResizableHashTable.MIN_SIZE, m.size)
        for i in range(ResizableHashTable.MIN_SIZE):
            m.put(i, 'foo')
        self.assertEqual(ResizableHashTable.MIN_SIZE * 2, m.size)
        self.assertEqual('foo', m.get(1))
        self.assertEqual('foo', m.get(3))
        self.assertEqual('foo', m.get(ResizableHashTable.MIN_SIZE - 1))
        
    def test_fill_up_the_limit(self):
        m = HashTable(10)
        for i in range(10):
            m.put(i,i**2)
        for i in range(10):
            self.assertEqual(i**2,m.get(i))

if __name__ == "__main__":
    unittest.main()
"""
Hash Table (Open Addressing)

Hash map implementation using open addressing with linear probing
for collision resolution. Includes a resizable variant that doubles
capacity when the load factor reaches two-thirds.

Reference: https://en.wikipedia.org/wiki/Open_addressing

Complexity:
    Time:  O(1) average for put/get/del, O(n) worst case
    Space: O(n)
"""

from __future__ import annotations


class HashTable:
    """Hash table using open addressing with linear probing.

    Examples:
        >>> ht = HashTable(10)
        >>> ht.put(1, 'one')
        >>> ht.get(1)
        'one'
    """

    _empty = object()
    _deleted = object()

    def __init__(self, size: int = 11) -> None:
        """Initialize the hash table.

        Args:
            size: Number of slots in the underlying array.
        """
        self.size = size
        self._len = 0
        self._keys: list[object] = [self._empty] * size
        self._values: list[object] = [self._empty] * size

    def put(self, key: int, value: object) -> None:
        """Insert or update a key-value pair.

        Args:
            key: The key to insert.
            value: The value associated with the key.

        Raises:
            ValueError: If the table is full.
        """
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty or self._keys[hash_] is self._deleted:
                self._keys[hash_] = key
                self._values[hash_] = value
                self._len += 1
                return
            elif self._keys[hash_] == key:
                self._keys[hash_] = key
                self._values[hash_] = value
                return

            hash_ = self._rehash(hash_)

            if initial_hash == hash_:
                raise ValueError("Table is full")

    def get(self, key: int) -> object | None:
        """Retrieve the value for a given key.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if not found.
        """
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                return None
            elif self._keys[hash_] == key:
                return self._values[hash_]

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                return None

    def del_(self, key: int) -> None:
        """Delete a key-value pair.

        Args:
            key: The key to delete.
        """
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                return None
            elif self._keys[hash_] == key:
                self._keys[hash_] = self._deleted
                self._values[hash_] = self._deleted
                self._len -= 1
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                return None

    def hash(self, key: int) -> int:
        """Compute the hash index for a key.

        Args:
            key: The key to hash.

        Returns:
            Index into the internal array.
        """
        return key % self.size

    def _rehash(self, old_hash: int) -> int:
        """Linear probing rehash.

        Args:
            old_hash: The previous hash index.

        Returns:
            Next index to probe.
        """
        return (old_hash + 1) % self.size

    def __getitem__(self, key: int) -> object | None:
        return self.get(key)

    def __delitem__(self, key: int) -> None:
        return self.del_(key)

    def __setitem__(self, key: int, value: object) -> None:
        self.put(key, value)

    def __len__(self) -> int:
        return self._len


class ResizableHashTable(HashTable):
    """Hash table that automatically doubles in size when load exceeds 2/3.

    Examples:
        >>> rht = ResizableHashTable()
        >>> rht.put(1, 'a')
        >>> rht.get(1)
        'a'
    """

    MIN_SIZE = 8

    def __init__(self) -> None:
        super().__init__(self.MIN_SIZE)

    def put(self, key: int, value: object) -> None:
        """Insert or update, resizing if load factor exceeds two-thirds.

        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        super().put(key, value)
        if len(self) >= (self.size * 2) / 3:
            self._resize()

    def _resize(self) -> None:
        """Double the table size and rehash all existing entries."""
        keys, values = self._keys, self._values
        self.size *= 2
        self._len = 0
        self._keys = [self._empty] * self.size
        self._values = [self._empty] * self.size
        for key, value in zip(keys, values, strict=False):
            if key is not self._empty and key is not self._deleted:
                self.put(key, value)

"""
Separate Chaining Hash Table

Hash table implementation using separate chaining (linked lists) for
collision resolution.

Reference: https://en.wikipedia.org/wiki/Hash_table#Separate_chaining

Complexity:
    Time:  O(1) average for put/get/del, O(n) worst case
    Space: O(n)
"""

from __future__ import annotations


class _Node:
    """Internal linked list node for chaining.

    Args:
        key: The key stored in this node.
        value: The value stored in this node.
        next_node: Reference to the next node in the chain.
    """

    def __init__(
        self,
        key: object = None,
        value: object = None,
        next_node: _Node | None = None,
    ) -> None:
        self.key = key
        self.value = value
        self.next = next_node


class SeparateChainingHashTable:
    """Hash table using separate chaining for collision resolution.

    Examples:
        >>> table = SeparateChainingHashTable()
        >>> table.put('hello', 'world')
        >>> len(table)
        1
        >>> table.get('hello')
        'world'
        >>> del table['hello']
        >>> table.get('hello') is None
        True
    """

    _empty = None

    def __init__(self, size: int = 11) -> None:
        """Initialize the hash table.

        Args:
            size: Number of buckets.
        """
        self.size = size
        self._len = 0
        self._table: list[_Node | None] = [self._empty] * size

    def put(self, key: object, value: object) -> None:
        """Insert or update a key-value pair.

        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        if node_ is self._empty:
            self._table[hash_] = _Node(key, value)
        else:
            while node_.next is not None:
                if node_.key == key:
                    node_.value = value
                    return
                node_ = node_.next
            node_.next = _Node(key, value)
        self._len += 1

    def get(self, key: object) -> object | None:
        """Retrieve the value for a given key.

        Args:
            key: The key to look up.

        Returns:
            The associated value, or None if the key is not found.
        """
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        while node_ is not self._empty:
            if node_.key == key:
                return node_.value
            node_ = node_.next
        return None

    def del_(self, key: object) -> None:
        """Delete a key-value pair.

        Args:
            key: The key to delete.
        """
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        previous_node = None
        while node_ is not None:
            if node_.key == key:
                if previous_node is None:
                    self._table[hash_] = node_.next
                else:
                    previous_node.next = node_.next
                self._len -= 1
            previous_node = node_
            node_ = node_.next

    def hash(self, key: object) -> int:
        """Compute the bucket index for a key.

        Args:
            key: The key to hash.

        Returns:
            Bucket index.
        """
        return hash(key) % self.size

    def __len__(self) -> int:
        return self._len

    def __getitem__(self, key: object) -> object | None:
        return self.get(key)

    def __delitem__(self, key: object) -> None:
        return self.del_(key)

    def __setitem__(self, key: object, value: object) -> None:
        self.put(key, value)

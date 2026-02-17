"""
Randomized Set

A data structure that supports insert, remove, and get-random-element
operations, all in average O(1) time.

Reference: https://leetcode.com/problems/insert-delete-getrandom-o1/

Complexity:
    Time:  O(1) average for insert, remove, and random_element
    Space: O(n)
"""

from __future__ import annotations

import random


class RandomizedSet:
    """A set supporting O(1) insert, remove, and random access."""

    def __init__(self) -> None:
        self.elements: list[int] = []
        self.index_map: dict[int, int] = {}

    def insert(self, new_one: int) -> None:
        """Insert a value into the set if not already present.

        Args:
            new_one: The value to insert.
        """
        if new_one in self.index_map:
            return
        self.index_map[new_one] = len(self.elements)
        self.elements.append(new_one)

    def remove(self, old_one: int) -> None:
        """Remove a value from the set if present.

        Args:
            old_one: The value to remove.
        """
        if old_one not in self.index_map:
            return
        index = self.index_map[old_one]
        last = self.elements.pop()
        self.index_map.pop(old_one)
        if index == len(self.elements):
            return
        self.elements[index] = last
        self.index_map[last] = index

    def random_element(self) -> int:
        """Return a random element from the set.

        Returns:
            A randomly chosen element.
        """
        return random.choice(self.elements)

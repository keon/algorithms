"""
Randomized Set

Design a data structure that supports insert, remove, and getRandom
in average O(1) time. Uses a list for random access and a dictionary
for O(1) lookup/removal.

Reference: https://leetcode.com/problems/insert-delete-getrandom-o1/

Complexity:
    Time:  O(1) average for insert, remove, get_random
    Space: O(n)
"""

from __future__ import annotations

import random


class RandomizedSet:
    """A set supporting O(1) insert, remove, and random element access.

    Examples:
        >>> rs = RandomizedSet()
        >>> rs.insert(1)
        True
        >>> rs.insert(1)
        False
        >>> rs.remove(1)
        True
    """

    def __init__(self) -> None:
        """Initialize the randomized set."""
        self.nums: list[int] = []
        self.idxs: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        """Insert a value into the set.

        Args:
            val: Value to insert.

        Returns:
            True if the value was inserted, False if already present.
        """
        if val not in self.idxs:
            self.nums.append(val)
            self.idxs[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """Remove a value from the set.

        Args:
            val: Value to remove.

        Returns:
            True if the value was removed, False if not present.
        """
        if val in self.idxs:
            idx, last = self.idxs[val], self.nums[-1]
            self.nums[idx], self.idxs[last] = last, idx
            self.nums.pop()
            self.idxs.pop(val, 0)
            return True
        return False

    def get_random(self) -> int:
        """Return a random element from the set.

        Returns:
            A randomly chosen element.
        """
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]

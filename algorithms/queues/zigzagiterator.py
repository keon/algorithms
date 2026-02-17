"""
Zigzag Iterator

Interleave elements from two lists in a zigzag fashion. Elements are
yielded alternately from each list until both are exhausted.

Reference: https://leetcode.com/problems/zigzag-iterator/

Complexity:
    Time:  O(n) total across all next() calls
    Space: O(n)
"""

from __future__ import annotations


class ZigZagIterator:
    """Iterator that interleaves elements from two lists.

    Examples:
        >>> it = ZigZagIterator([1, 2], [3, 4, 5])
        >>> it.next()
        1
        >>> it.next()
        3
    """

    def __init__(self, v1: list[int], v2: list[int]) -> None:
        """Initialize with two lists.

        Args:
            v1: First input list.
            v2: Second input list.
        """
        self.queue: list[list[int]] = [lst for lst in (v1, v2) if lst]

    def next(self) -> int:
        """Return the next element in zigzag order.

        Returns:
            The next interleaved element.
        """
        current_list = self.queue.pop(0)
        ret = current_list.pop(0)
        if current_list:
            self.queue.append(current_list)
        return ret

    def has_next(self) -> bool:
        """Check if there are more elements.

        Returns:
            True if elements remain, False otherwise.
        """
        if self.queue:
            return True
        return False

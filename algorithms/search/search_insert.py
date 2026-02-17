"""
Search Insert Position

Given a sorted array and a target value, return the index if the target is
found.  If not, return the index where it would be if it were inserted in
order.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(1) best / O(log n) average / O(log n) worst
    Space: O(1)
"""

from __future__ import annotations


def search_insert(array: list[int], val: int) -> int:
    """Return the index of *val* or the position where it should be inserted.

    Args:
        array: Sorted list of integers in ascending order.
        val: Value to search for or insert.

    Returns:
        Index of *val* in *array*, or the index at which *val* would be
        inserted to keep *array* sorted.

    Examples:
        >>> search_insert([1, 3, 5, 6], 5)
        2
        >>> search_insert([1, 3, 5, 6], 2)
        1
        >>> search_insert([1, 3, 5, 6], 7)
        4
        >>> search_insert([1, 3, 5, 6], 0)
        0
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if val > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low

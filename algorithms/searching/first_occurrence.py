"""
First Occurrence

Find the index of the first occurrence of a target value in a sorted array
using binary search.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(1) best / O(log n) average / O(log n) worst
    Space: O(1)
"""

from __future__ import annotations


def first_occurrence(array: list[int], query: int) -> int:
    """Find the index of the first occurrence of *query* in *array*.

    Args:
        array: Sorted list of integers in ascending order.
        query: Value to search for.

    Returns:
        Index of the first occurrence of *query*, or -1 if not found.

    Examples:
        >>> first_occurrence([1, 2, 2, 2, 3, 4], 2)
        1
        >>> first_occurrence([1, 2, 3, 4, 5], 6)
        -1
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if low == high:
            break
        if array[mid] < query:
            low = mid + 1
        else:
            high = mid
    if array[low] == query:
        return low
    return -1

"""
Last Occurrence

Find the index of the last occurrence of a target value in a sorted array
using binary search.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(1) best / O(log n) average / O(log n) worst
    Space: O(1)
"""

from __future__ import annotations


def last_occurrence(array: list[int], query: int) -> int:
    """Find the index of the last occurrence of *query* in *array*.

    Args:
        array: Sorted list of integers in ascending order.
        query: Value to search for.

    Returns:
        Index of the last occurrence of *query*, or -1 if not found.

    Examples:
        >>> last_occurrence([1, 2, 2, 2, 3, 4], 2)
        3
        >>> last_occurrence([1, 2, 3, 4, 5], 6)
        -1
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if (array[mid] == query and mid == len(array) - 1) or (
            array[mid] == query and array[mid + 1] > query
        ):
            return mid
        if array[mid] <= query:
            low = mid + 1
        else:
            high = mid - 1
    return -1

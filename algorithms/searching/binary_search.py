"""
Binary Search

Search for an element in a sorted array by repeatedly dividing the search
interval in half.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(1) best / O(log n) average / O(log n) worst
    Space: O(1) iterative, O(log n) recursive
"""

from __future__ import annotations


def binary_search(array: list[int], query: int) -> int:
    """Search for *query* in a sorted *array* using iterative binary search.

    Args:
        array: Sorted list of integers in ascending order.
        query: Value to search for.

    Returns:
        Index of *query* in *array*, or -1 if not found.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        val = array[mid]
        if val == query:
            return mid
        if val < query:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recur(array: list[int], low: int, high: int, val: int) -> int:
    """Search for *val* in a sorted *array* using recursive binary search.

    Args:
        array: Sorted list of integers in ascending order.
        low: Lower bound index of the current search range.
        high: Upper bound index of the current search range.
        val: Value to search for.

    Returns:
        Index of *val* in *array*, or -1 if not found.

    Examples:
        >>> binary_search_recur([1, 2, 3, 4, 5], 0, 4, 3)
        2
        >>> binary_search_recur([1, 2, 3, 4, 5], 0, 4, 6)
        -1
    """
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    if val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    return mid

"""
Linear Search

Search for a target value in an array by checking every element sequentially.
The array does not need to be sorted.

Reference: https://en.wikipedia.org/wiki/Linear_search

Complexity:
    Time:  O(1) best / O(n) average / O(n) worst
    Space: O(1)
"""

from __future__ import annotations


def linear_search(array: list[int], query: int) -> int:
    """Search for *query* in *array* using linear search.

    Args:
        array: List of integers (order does not matter).
        query: Value to search for.

    Returns:
        Index of *query* in *array*, or -1 if not found.

    Examples:
        >>> linear_search([5, 1, 3, 2, 4], 3)
        2
        >>> linear_search([5, 1, 3, 2, 4], 6)
        -1
    """
    for i, value in enumerate(array):
        if value == query:
            return i
    return -1

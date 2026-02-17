"""
Exchange Sort

Exchange sort compares every pair of elements and swaps them if they are
out of order.  It is conceptually similar to bubble sort.

Reference: https://en.wikipedia.org/wiki/Sorting_algorithm#Exchange_sort

Complexity:
    Time:  O(n^2) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def exchange_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using exchange sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> exchange_sort([3, 1, 2])
        [1, 2, 3]
    """
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

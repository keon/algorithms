"""
Bogo Sort

Bogo sort repeatedly shuffles the array at random until it happens to be
sorted.  It is extremely inefficient and used only for educational purposes.

Reference: https://en.wikipedia.org/wiki/Bogosort

Complexity:
    Time:  O(n) best / O(n * n!) average / O(infinity) worst
    Space: O(1)
"""

from __future__ import annotations

import random


def bogo_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using bogo sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> bogo_sort([3, 1, 2])
        [1, 2, 3]
    """
    while not _is_sorted(array):
        random.shuffle(array)
    return array


def _is_sorted(array: list[int]) -> bool:
    """Return True if *array* is in non-decreasing order."""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

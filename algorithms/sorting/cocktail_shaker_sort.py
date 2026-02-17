"""
Cocktail Shaker Sort

Cocktail shaker sort is a variation of bubble sort that traverses the
list alternately from left-to-right and right-to-left.

Reference: https://en.wikipedia.org/wiki/Cocktail_shaker_sort

Complexity:
    Time:  O(n) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def cocktail_shaker_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using cocktail shaker sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> cocktail_shaker_sort([3, 1, 2])
        [1, 2, 3]
    """
    n = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True
        if not swapped:
            return array
        swapped = False
        for i in range(n - 1, 0, -1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True
    return array

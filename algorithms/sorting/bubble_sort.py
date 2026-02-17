"""
Bubble Sort

Bubble sort repeatedly steps through the list, compares adjacent elements
and swaps them if they are in the wrong order.

Reference: https://en.wikipedia.org/wiki/Bubble_sort

Complexity:
    Time:  O(n) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def bubble_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using bubble sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> bubble_sort([3, 1, 2])
        [1, 2, 3]
    """
    n = len(array)
    swapped = True
    passes = 0
    while swapped:
        swapped = False
        for i in range(1, n - passes):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True
        passes += 1
    return array

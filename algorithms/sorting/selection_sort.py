"""
Selection Sort

Selection sort repeatedly selects the smallest element from the unsorted
portion and moves it to the end of the sorted portion.

Reference: https://en.wikipedia.org/wiki/Selection_sort

Complexity:
    Time:  O(n^2) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def selection_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using selection sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> selection_sort([3, 1, 2])
        [1, 2, 3]
    """
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]
    return array

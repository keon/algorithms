"""
Quick Sort

Quick sort selects a pivot element, partitions the array around the
pivot, and recursively sorts the two partitions.

Reference: https://en.wikipedia.org/wiki/Quicksort

Complexity:
    Time:  O(n log n) best / O(n log n) average / O(n^2) worst
    Space: O(log n)
"""

from __future__ import annotations


def quick_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using quick sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> quick_sort([3, 1, 2])
        [1, 2, 3]
    """
    _quick_sort_recursive(array, 0, len(array) - 1)
    return array


def _quick_sort_recursive(array: list[int], first: int, last: int) -> None:
    """Recursively sort *array[first..last]* in-place."""
    if first < last:
        pivot = _partition(array, first, last)
        _quick_sort_recursive(array, first, pivot - 1)
        _quick_sort_recursive(array, pivot + 1, last)


def _partition(array: list[int], first: int, last: int) -> int:
    """Partition *array[first..last]* using the last element as pivot.

    Returns:
        The final index of the pivot element.
    """
    wall = first
    for pos in range(first, last):
        if array[pos] < array[last]:
            array[pos], array[wall] = array[wall], array[pos]
            wall += 1
    array[wall], array[last] = array[last], array[wall]
    return wall

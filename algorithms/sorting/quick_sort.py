"""
Quick Sort

Quick sort selects a pivot element, partitions the array around the
pivot, and recursively sorts the two partitions.

This implementation uses Median-of-Three pivot selection and switches to
Insertion Sort for small subarrays to improve performance and avoid
O(n^2) worst-case on nearly sorted arrays.

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
    # Threshold for switching to insertion sort
    if last - first < 10:
        _insertion_sort(array, first, last)
        return

    if first < last:
        pivot = _partition(array, first, last)
        _quick_sort_recursive(array, first, pivot - 1)
        _quick_sort_recursive(array, pivot + 1, last)


def _insertion_sort(array: list[int], first: int, last: int) -> None:
    """Sort *array[first..last]* in-place using insertion sort."""
    for i in range(first + 1, last + 1):
        key = array[i]
        j = i - 1
        while j >= first and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def _partition(array: list[int], first: int, last: int) -> int:
    """Partition *array[first..last]* using Median-of-Three pivot.

    Returns:
        The final index of the pivot element.
    """
    # Median-of-Three pivot selection
    mid = (first + last) // 2
    if array[first] > array[mid]:
        array[first], array[mid] = array[mid], array[first]
    if array[first] > array[last]:
        array[first], array[last] = array[last], array[first]
    if array[mid] > array[last]:
        array[mid], array[last] = array[last], array[mid]
    
    # Move pivot to the end
    array[mid], array[last] = array[last], array[mid]
    pivot = array[last]
    
    wall = first
    for pos in range(first, last):
        if array[pos] < pivot:
            array[pos], array[wall] = array[wall], array[pos]
            wall += 1
    array[wall], array[last] = array[last], array[wall]
    return wall

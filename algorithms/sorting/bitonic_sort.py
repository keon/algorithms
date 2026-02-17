"""
Bitonic Sort

Bitonic sort is a comparison-based sorting algorithm designed for parallel
execution.  This implementation is sequential.  The input size must be a
power of two.

Reference: https://en.wikipedia.org/wiki/Bitonic_sorter

Complexity:
    Time:  O(n log^2 n) best / O(n log^2 n) average / O(n log^2 n) worst
    Space: O(n log^2 n)
"""

from __future__ import annotations


def bitonic_sort(array: list[int], reverse: bool = False) -> list[int]:
    """Sort an array using bitonic sort.

    Args:
        array:   List of integers to sort.
        reverse: If True, sort in descending order.

    Returns:
        A sorted list.

    Raises:
        ValueError: If the array length is not a power of two.

    Examples:
        >>> bitonic_sort([4, 2, 1, 3])
        [1, 2, 3, 4]
    """
    n = len(array)
    if n <= 1:
        return array
    if not (n and not (n & (n - 1))):
        raise ValueError("the size of input should be power of two")

    left = bitonic_sort(array[:n // 2], True)
    right = bitonic_sort(array[n // 2:], False)
    return _bitonic_merge(left + right, reverse)


def _compare(array: list[int], reverse: bool) -> list[int]:
    """Compare and swap elements across the two halves of *array*."""
    half = len(array) // 2
    for i in range(half):
        if reverse != (array[i] > array[i + half]):
            array[i], array[i + half] = array[i + half], array[i]
    return array


def _bitonic_merge(array: list[int], reverse: bool) -> list[int]:
    """Recursively merge a bitonic sequence into sorted order."""
    n = len(array)
    if n <= 1:
        return array

    array = _compare(array, reverse)
    left = _bitonic_merge(array[:n // 2], reverse)
    right = _bitonic_merge(array[n // 2:], reverse)
    return left + right

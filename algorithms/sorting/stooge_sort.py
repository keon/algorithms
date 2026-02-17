"""
Stooge Sort

Stooge sort is a recursive sorting algorithm notable for its unusually
bad time complexity.  It works by recursively sorting the first 2/3, then
the last 2/3, and then the first 2/3 again.

Reference: https://en.wikipedia.org/wiki/Stooge_sort

Complexity:
    Time:  O(n^2.709) best / O(n^2.709) average / O(n^2.709) worst
    Space: O(n)
"""

from __future__ import annotations


def stooge_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using stooge sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> stooge_sort([3, 1, 2])
        [1, 2, 3]
    """
    _stooge_sort(array, 0, len(array) - 1)
    return array


def _stooge_sort(array: list[int], low: int, high: int) -> None:
    """Recursively sort *array[low..high]* using stooge sort."""
    if low >= high:
        return

    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]

    if high - low + 1 > 2:
        third = (high - low + 1) // 3
        _stooge_sort(array, low, high - third)
        _stooge_sort(array, low + third, high)
        _stooge_sort(array, low, high - third)

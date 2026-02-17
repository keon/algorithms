"""
Shell Sort

Shell sort is a generalisation of insertion sort that allows the exchange
of elements that are far apart.  The gap between compared elements is
gradually reduced until it becomes 1, at which point the algorithm
behaves like a standard insertion sort.

Reference: https://en.wikipedia.org/wiki/Shellsort

Complexity:
    Time:  O(n log n) best / O(n^(4/3)) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def shell_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using shell sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> shell_sort([3, 1, 2])
        [1, 2, 3]
    """
    n = len(array)
    gap = n // 2

    while gap > 0:
        y_index = gap
        while y_index < n:
            y = array[y_index]
            x_index = y_index - gap
            while x_index >= 0 and y < array[x_index]:
                array[x_index + gap] = array[x_index]
                x_index -= gap
            array[x_index + gap] = y
            y_index += 1
        gap //= 2

    return array

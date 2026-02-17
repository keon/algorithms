"""
Gnome Sort

Gnome sort moves an element toward the front of the list until it finds
an element that is smaller or equal, then steps forward again.  It is
similar to insertion sort but uses swaps instead of shifts.

Reference: https://en.wikipedia.org/wiki/Gnome_sort

Complexity:
    Time:  O(n) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def gnome_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using gnome sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> gnome_sort([3, 1, 2])
        [1, 2, 3]
    """
    n = len(array)
    index = 0
    while index < n:
        if index == 0 or array[index] >= array[index - 1]:
            index += 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1
    return array

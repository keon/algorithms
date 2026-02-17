"""
Comb Sort

Comb sort improves on bubble sort by using a gap sequence that shrinks by
a factor of approximately 1.3 on each pass, eliminating small values near
the end of the list (known as "turtles") more quickly.

Reference: https://en.wikipedia.org/wiki/Comb_sort

Complexity:
    Time:  O(n log n) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def comb_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using comb sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> comb_sort([3, 1, 2])
        [1, 2, 3]
    """
    n = len(array)
    gap = n
    shrink_factor = 1.3
    is_sorted = False

    while not is_sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            is_sorted = True

        i = 0
        while i + gap < n:
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                is_sorted = False
            i += 1

    return array

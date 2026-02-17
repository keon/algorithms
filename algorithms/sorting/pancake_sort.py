"""
Pancake Sort

Pancake sort sorts an array by repeatedly finding the maximum element in
the unsorted portion, flipping it to the front, and then flipping the
entire unsorted portion so the maximum lands at the end.

Reference: https://en.wikipedia.org/wiki/Pancake_sorting

Complexity:
    Time:  O(n) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def pancake_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using pancake sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> pancake_sort([3, 1, 2])
        [1, 2, 3]
    """
    if len(array) <= 1:
        return array

    for cur in range(len(array), 1, -1):
        index_max = array.index(max(array[0:cur]))
        if index_max + 1 != cur:
            if index_max != 0:
                array[: index_max + 1] = reversed(array[: index_max + 1])
            array[:cur] = reversed(array[:cur])
    return array

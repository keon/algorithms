"""
Wiggle Sort

Given an unsorted array, reorder it in-place such that
nums[0] < nums[1] > nums[2] < nums[3] ...

Reference: https://leetcode.com/problems/wiggle-sort/

Complexity:
    Time:  O(n) best / O(n) average / O(n) worst
    Space: O(1)
"""

from __future__ import annotations


def wiggle_sort(array: list[int]) -> list[int]:
    """Reorder *array* in-place into wiggle-sorted order.

    Args:
        array: List of integers to reorder.

    Returns:
        The wiggle-sorted list.

    Examples:
        >>> wiggle_sort([3, 5, 2, 1, 6, 4])
        [3, 5, 1, 6, 2, 4]
    """
    for i in range(len(array)):
        if (i % 2 == 1) == (array[i - 1] > array[i]):
            array[i - 1], array[i] = array[i], array[i - 1]
    return array

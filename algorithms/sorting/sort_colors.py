"""
Sort Colors (Dutch National Flag)

Given an array with n objects colored red, white, or blue (represented by
0, 1, and 2), sort them in-place so that objects of the same color are
adjacent, with the colors in order red, white, blue.

Reference: https://leetcode.com/problems/sort-colors/

Complexity:
    Time:  O(n) best / O(n) average / O(n) worst
    Space: O(1)
"""

from __future__ import annotations


def sort_colors(array: list[int]) -> list[int]:
    """Sort an array of 0s, 1s, and 2s in-place.

    Args:
        array: List of integers (each 0, 1, or 2) to sort.

    Returns:
        The sorted list.

    Examples:
        >>> sort_colors([2, 0, 1, 2, 1, 0])
        [0, 0, 1, 1, 2, 2]
    """
    red = white = 0
    for k in range(len(array)):
        value = array[k]
        array[k] = 2
        if value < 2:
            array[white] = 1
            white += 1
        if value == 0:
            array[red] = 0
            red += 1
    return array

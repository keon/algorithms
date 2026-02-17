"""
Ternary Search

Search for a target value in a sorted array by dividing the search range into
three equal parts instead of two.  At each step two midpoints are computed and
the search range is narrowed to one third.

Reference: https://en.wikipedia.org/wiki/Ternary_search

Complexity:
    Time:  O(1) best / O(log3 n) average / O(log3 n) worst
    Space: O(1)
"""

from __future__ import annotations


def ternary_search(left: int, right: int, key: int, array: list[int]) -> int:
    """Search for *key* in a sorted *array* using ternary search.

    Args:
        left: Lower bound index of the search range (inclusive).
        right: Upper bound index of the search range (inclusive).
        key: Value to search for.
        array: Sorted list of integers in ascending order.

    Returns:
        Index of *key* in *array*, or -1 if not found within the range.

    Examples:
        >>> ternary_search(0, 8, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        4
        >>> ternary_search(0, 4, 0, [1, 2, 3, 4, 5])
        -1
    """
    while right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if key == array[mid1]:
            return mid1
        if key == array[mid2]:
            return mid2

        if key < array[mid1]:
            right = mid1 - 1
        elif key > array[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

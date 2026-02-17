"""
Search in Rotated Sorted Array

Search for a target value in an array that was sorted in ascending order and
then rotated at some unknown pivot.  One half of the array is always in sorted
order; we identify that half and decide which side to search.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(1) best / O(log n) average / O(log n) worst
    Space: O(1) iterative, O(log n) recursive
"""

from __future__ import annotations


def search_rotate(array: list[int], val: int) -> int:
    """Search for *val* in a rotated sorted *array* (iterative).

    Args:
        array: A sorted list of integers that has been rotated at an
            unknown pivot.
        val: Value to search for.

    Returns:
        Index of *val* in *array*, or -1 if not found.

    Examples:
        >>> search_rotate([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> search_rotate([4, 5, 6, 7, 0, 1, 2], 3)
        -1
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if val == array[mid]:
            return mid

        if array[low] <= array[mid]:
            if array[low] <= val <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if array[mid] <= val <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def search_rotate_recur(
    array: list[int],
    low: int,
    high: int,
    val: int,
) -> int:
    """Search for *val* in a rotated sorted *array* (recursive).

    Args:
        array: A sorted list of integers that has been rotated at an
            unknown pivot.
        low: Lower bound index of the current search range.
        high: Upper bound index of the current search range.
        val: Value to search for.

    Returns:
        Index of *val* in *array*, or -1 if not found.

    Examples:
        >>> search_rotate_recur([4, 5, 6, 7, 0, 1, 2], 0, 6, 0)
        4
    """
    if low >= high:
        return -1
    mid = (low + high) // 2
    if val == array[mid]:
        return mid
    if array[low] <= array[mid]:
        if array[low] <= val <= array[mid]:
            return search_rotate_recur(array, low, mid - 1, val)
        return search_rotate_recur(array, mid + 1, high, val)
    if array[mid] <= val <= array[high]:
        return search_rotate_recur(array, mid + 1, high, val)
    return search_rotate_recur(array, low, mid - 1, val)

"""
Merge Sort

Merge sort divides the array in half, recursively sorts each half, and
then merges the two sorted halves back together.

Reference: https://en.wikipedia.org/wiki/Merge_sort

Complexity:
    Time:  O(n log n) best / O(n log n) average / O(n log n) worst
    Space: O(n)
"""

from __future__ import annotations


def merge_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using merge sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> merge_sort([3, 1, 2])
        [1, 2, 3]
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    _merge(left, right, array)
    return array


def _merge(left: list[int], right: list[int], merged: list[int]) -> None:
    """Merge two sorted lists into *merged* in-place.

    Args:
        left:   Sorted left half.
        right:  Sorted right half.
        merged: Destination list (length == len(left) + len(right)).
    """
    left_cursor = 0
    right_cursor = 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):  # noqa: B020
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):  # noqa: B020
        merged[left_cursor + right_cursor] = right[right_cursor]

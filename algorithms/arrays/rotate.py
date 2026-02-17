"""
Rotate Array

Rotate an array of n elements to the right by k steps.
Three algorithm variants are provided with different time complexities.

Reference: https://leetcode.com/problems/rotate-array/

Complexity:
    rotate_v1: Time O(n*k), Space O(n)
    rotate_v2: Time O(n),   Space O(n)
    rotate_v3: Time O(n),   Space O(n)
"""

from __future__ import annotations


def rotate_v1(array: list[int], k: int) -> list[int]:
    """Rotate array to the right by k steps using repeated single shifts.

    Args:
        array: List of integers to rotate.
        k: Number of positions to rotate right.

    Returns:
        New rotated list.

    Examples:
        >>> rotate_v1([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
    """
    array = array[:]
    length = len(array)
    for _ in range(k):
        temp = array[length - 1]
        for position in range(length - 1, 0, -1):
            array[position] = array[position - 1]
        array[0] = temp
    return array


def rotate_v2(array: list[int], k: int) -> list[int]:
    """Rotate array to the right by k steps using three reversals.

    Args:
        array: List of integers to rotate.
        k: Number of positions to rotate right.

    Returns:
        New rotated list.

    Examples:
        >>> rotate_v2([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
    """
    array = array[:]

    def _reverse(arr: list[int], left: int, right: int) -> None:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    length = len(array)
    k = k % length
    _reverse(array, 0, length - k - 1)
    _reverse(array, length - k, length - 1)
    _reverse(array, 0, length - 1)
    return array


def rotate_v3(array: list[int] | None, k: int) -> list[int] | None:
    """Rotate array to the right by k steps using slicing.

    Args:
        array: List of integers to rotate, or None.
        k: Number of positions to rotate right.

    Returns:
        New rotated list, or None if input is None.

    Examples:
        >>> rotate_v3([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
    """
    if array is None:
        return None
    length = len(array)
    k = k % length
    return array[length - k:] + array[:length - k]

"""
Counting Sort

Counting sort counts the occurrences of each value and uses cumulative
counts to place each element in its correct position.  It supports
negative integers by shifting values internally.

Reference: https://en.wikipedia.org/wiki/Counting_sort

Complexity:
    Time:  O(n + k) best / O(n + k) average / O(n + k) worst
    Space: O(n + k)   where k is the range of input values
"""

from __future__ import annotations


def counting_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using counting sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> counting_sort([3, 1, 2])
        [1, 2, 3]
    """
    min_value = min(array)
    offset = -min_value if min_value < 0 else 0

    shifted = [v + offset for v in array]
    max_value = max(shifted)

    counts = [0] * (max_value + 1)
    for value in shifted:
        counts[value] += 1

    # Build cumulative counts
    for i in range(1, max_value + 1):
        counts[i] += counts[i - 1]

    result = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):
        value = shifted[i]
        counts[value] -= 1
        result[counts[value]] = value - offset
    return result

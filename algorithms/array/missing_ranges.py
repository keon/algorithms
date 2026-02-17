"""
Missing Ranges

Find the ranges of numbers that are missing between a given low and high
bound, given a sorted array of integers.

Reference: https://leetcode.com/problems/missing-ranges/

Complexity:
    Time:  O(n)
    Space: O(n) for the result list
"""

from __future__ import annotations


def missing_ranges(
    array: list[int], low: int, high: int
) -> list[tuple[int, int]]:
    """Find gaps between low and high not covered by elements in array.

    Args:
        array: Sorted list of integers within [low, high].
        low: Lower bound of the expected range (inclusive).
        high: Upper bound of the expected range (inclusive).

    Returns:
        List of (start, end) tuples representing missing ranges.

    Examples:
        >>> missing_ranges([3, 5], 1, 10)
        [(1, 2), (4, 4), (6, 10)]
    """
    result = []
    start = low

    for num in array:
        if num == start:
            start += 1
        elif num > start:
            result.append((start, num - 1))
            start = num + 1

    if start <= high:
        result.append((start, high))

    return result

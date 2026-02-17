"""
Summarize Ranges

Given a sorted integer array without duplicates, return the summary of its
ranges as a list of (start, end) tuples.

Reference: https://leetcode.com/problems/summary-ranges/

Complexity:
    Time:  O(n)
    Space: O(n) for the result list
"""

from __future__ import annotations


def summarize_ranges(array: list[int]) -> list[tuple[int, ...]]:
    """Summarize consecutive runs in a sorted array as (start, end) tuples.

    Args:
        array: Sorted list of unique integers.

    Returns:
        List of (start, end) tuples for each consecutive range.

    Examples:
        >>> summarize_ranges([0, 1, 2, 4, 5, 7])
        [(0, 2), (4, 5), (7, 7)]
    """
    result = []
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [(array[0], array[0])]
    iterator = iter(array)
    start = end = next(iterator)
    for num in iterator:
        if num - end == 1:
            end = num
        else:
            result.append((start, end))
            start = end = num
    result.append((start, end))
    return result

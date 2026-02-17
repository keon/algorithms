"""
Two Sum

Given an array of integers and a target sum, return the indices of the two
numbers that add up to the target.

Reference: https://leetcode.com/problems/two-sum/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def two_sum(array: list[int], target: int) -> tuple[int, int] | None:
    """Find two indices whose corresponding values sum to target.

    Args:
        array: List of integers to search.
        target: Desired sum of two elements.

    Returns:
        Tuple of (index1, index2) if a pair is found, or None otherwise.

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
    """
    seen = {}
    for index, num in enumerate(array):
        if num in seen:
            return seen[num], index
        else:
            seen[target - num] = index
    return None

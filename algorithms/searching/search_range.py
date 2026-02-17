"""
Search Range

Given a sorted array of integers and a target value, find the starting and
ending positions of the target.  Returns [-1, -1] if the target is not found.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(log n + k) where k is the number of occurrences in the worst
           case for the backward scan, O(log n) for the initial search
    Space: O(1)
"""

from __future__ import annotations


def search_range(nums: list[int], target: int) -> list[int]:
    """Find the first and last positions of *target* in *nums*.

    Args:
        nums: Sorted list of integers in ascending order.
        target: Value to search for.

    Returns:
        A two-element list ``[first, last]`` of indices, or ``[-1, -1]``
        if *target* is not present.

    Examples:
        >>> search_range([5, 7, 7, 8, 8, 8, 10], 8)
        [3, 5]
        >>> search_range([5, 7, 7, 8, 8, 8, 10], 11)
        [-1, -1]
    """
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2
        if target <= nums[mid]:
            high = mid
        else:
            low = mid + 1

    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == target:
            return [low, j]

    return [-1, -1]

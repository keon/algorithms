"""
Combination Sum

Given a set of candidate numbers (without duplicates) and a target number,
find all unique combinations where the candidate numbers sum to the target.
The same number may be chosen an unlimited number of times.

Reference: https://leetcode.com/problems/combination-sum/

Complexity:
    Time:  O(n^(T/M)) where T is target, M is minimum candidate
    Space: O(T/M) recursion depth
"""

from __future__ import annotations


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Find all unique combinations of candidates that sum to target.

    Args:
        candidates: A list of distinct positive integers.
        target: The target sum.

    Returns:
        A list of lists, each containing a valid combination.

    Examples:
        >>> combination_sum([2, 3, 6, 7], 7)
        [[2, 2, 3], [7]]
    """
    result: list[list[int]] = []
    candidates.sort()
    _dfs(candidates, target, 0, [], result)
    return result


def _dfs(
    nums: list[int],
    target: int,
    index: int,
    path: list[int],
    result: list[list[int]],
) -> None:
    """Depth-first search helper for building combinations."""
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(index, len(nums)):
        _dfs(nums, target - nums[i], i, path + [nums[i]], result)

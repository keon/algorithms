"""
Unique Subsets

Given a collection of integers that might contain duplicates, return all
possible unique subsets (the power set without duplicates).

Reference: https://leetcode.com/problems/subsets-ii/

Complexity:
    Time:  O(2^n) where n is the number of elements
    Space: O(2^n) to store all subsets
"""

from __future__ import annotations


def subsets_unique(nums: list[int]) -> list[tuple[int, ...]]:
    """Return all unique subsets of a list that may have duplicates.

    Args:
        nums: A list of integers, possibly with duplicates.

    Returns:
        A list of unique tuples representing each subset.

    Examples:
        >>> sorted(subsets_unique([1, 2, 2]))
        [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)]
    """
    found: set[tuple[int, ...]] = set()
    _backtrack(found, nums, [], 0)
    return list(found)


def _backtrack(
    found: set[tuple[int, ...]],
    nums: list[int],
    stack: list[int],
    position: int,
) -> None:
    """Recursive helper that includes or excludes each element."""
    if position == len(nums):
        found.add(tuple(stack))
    else:
        stack.append(nums[position])
        _backtrack(found, nums, stack, position + 1)
        stack.pop()
        _backtrack(found, nums, stack, position + 1)

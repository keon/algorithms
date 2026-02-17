"""
Subsets

Given a set of distinct integers, return all possible subsets (the power
set). The solution set must not contain duplicate subsets.

Reference: https://en.wikipedia.org/wiki/Power_set

Complexity:
    Time:  O(2^n) where n is the number of elements
    Space: O(2^n) to store all subsets
"""

from __future__ import annotations


def subsets(nums: list[int]) -> list[list[int]]:
    """Return all subsets of the given list using backtracking.

    Args:
        nums: A list of distinct integers.

    Returns:
        A list of all subsets.

    Examples:
        >>> sorted(subsets([1, 2]), key=str)
        [[], [1], [1, 2], [2]]
    """
    result: list[list[int]] = []
    _backtrack(result, nums, [], 0)
    return result


def _backtrack(
    result: list[list[int]],
    nums: list[int],
    stack: list[int],
    position: int,
) -> None:
    """Recursive helper that includes or excludes each element."""
    if position == len(nums):
        result.append(list(stack))
    else:
        stack.append(nums[position])
        _backtrack(result, nums, stack, position + 1)
        stack.pop()
        _backtrack(result, nums, stack, position + 1)


def subsets_v2(nums: list[int]) -> list[list[int]]:
    """Return all subsets of the given list using iteration.

    Builds subsets iteratively by extending each existing subset
    with the next element.

    Args:
        nums: A list of distinct integers.

    Returns:
        A list of all subsets.

    Examples:
        >>> sorted(subsets_v2([1, 2]), key=str)
        [[], [1], [1, 2], [2]]
    """
    result: list[list[int]] = [[]]
    for number in sorted(nums):
        result += [item + [number] for item in result]
    return result

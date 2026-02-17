"""
Permutations

Given a collection of distinct elements, return all possible permutations.

Reference: https://en.wikipedia.org/wiki/Permutation

Complexity:
    Time:  O(n * n!) where n is the number of elements
    Space: O(n * n!) to store all permutations
"""

from __future__ import annotations

from typing import Generator


def permute(elements: list | str) -> list:
    """Return all permutations of the given elements.

    Args:
        elements: A list or string of distinct elements.

    Returns:
        A list of all permutations (same type as input elements).

    Examples:
        >>> permute([1, 2, 3])
        [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
    """
    if len(elements) <= 1:
        return [elements]
    result = []
    for perm in permute(elements[1:]):
        for i in range(len(elements)):
            result.append(perm[:i] + elements[0:1] + perm[i:])
    return result


def permute_iter(elements: list | str) -> Generator:
    """Yield all permutations of the given elements one at a time.

    Args:
        elements: A list or string of distinct elements.

    Yields:
        One permutation at a time (same type as input elements).

    Examples:
        >>> list(permute_iter([1, 2]))
        [[1, 2], [2, 1]]
    """
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permute_iter(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def permute_recursive(nums: list[int]) -> list[list[int]]:
    """Return all permutations using DFS backtracking.

    Args:
        nums: A list of distinct integers.

    Returns:
        A list of all permutations.

    Examples:
        >>> sorted(permute_recursive([1, 2]))
        [[1, 2], [2, 1]]
    """
    result: list[list[int]] = []
    _dfs(result, nums, [])
    return result


def _dfs(
    result: list[list[int]],
    nums: list[int],
    path: list[int],
) -> None:
    """DFS helper that builds permutations by choosing remaining elements."""
    if not nums:
        result.append(path)
    for i in range(len(nums)):
        _dfs(result, nums[:i] + nums[i + 1:], path + [nums[i]])

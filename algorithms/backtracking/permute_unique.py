"""
Unique Permutations

Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

Reference: https://leetcode.com/problems/permutations-ii/

Complexity:
    Time:  O(n * n!) worst case
    Space: O(n * n!) to store all unique permutations
"""

from __future__ import annotations


def permute_unique(nums: list[int]) -> list[list[int]]:
    """Return all unique permutations of a list that may have duplicates.

    Args:
        nums: A list of integers, possibly with duplicates.

    Returns:
        A list of all unique permutations.

    Examples:
        >>> sorted(permute_unique([1, 1, 2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    """
    permutations: list[list[int]] = [[]]
    for number in nums:
        new_permutations: list[list[int]] = []
        for existing in permutations:
            for i in range(len(existing) + 1):
                new_permutations.append(existing[:i] + [number] + existing[i:])
                if i < len(existing) and existing[i] == number:
                    break
        permutations = new_permutations
    return permutations

"""
Array Sum Combinations

Given three arrays and a target sum, find all three-element combinations
(one element from each array) that add up to the target.

Reference: https://en.wikipedia.org/wiki/Subset_sum_problem

Complexity:
    Time:  O(n^3) brute-force product of three arrays
    Space: O(k) where k is the number of valid combinations
"""

from __future__ import annotations

import itertools
from functools import partial


def array_sum_combinations(
    array_a: list[int],
    array_b: list[int],
    array_c: list[int],
    target: int,
) -> list[list[int]]:
    """Find all combinations of one element per array that sum to target.

    Uses backtracking to enumerate valid combinations, allowing duplicates.

    Args:
        array_a: First array of integers.
        array_b: Second array of integers.
        array_c: Third array of integers.
        target: The desired sum.

    Returns:
        A list of three-element lists that sum to target.

    Examples:
        >>> array_sum_combinations([1], [2], [3], 6)
        [[1, 2, 3]]
    """
    arrays = [array_a, array_b, array_c]

    def _is_complete(constructed_so_far: list[int]) -> tuple[bool, bool]:
        total = sum(constructed_so_far)
        should_stop = total >= target or len(constructed_so_far) >= 3
        reached_target = total == target and len(constructed_so_far) == 3
        return should_stop, reached_target

    def _get_candidates(constructed_so_far: list[int]) -> list[int]:
        return arrays[len(constructed_so_far)]

    def _backtrack(
        constructed_so_far: list[int] | None = None,
        result: list[list[int]] | None = None,
    ) -> None:
        if constructed_so_far is None:
            constructed_so_far = []
        if result is None:
            result = []
        should_stop, reached_target = _is_complete(constructed_so_far)
        if should_stop:
            if reached_target:
                result.append(constructed_so_far)
            return
        candidates = _get_candidates(constructed_so_far)
        for candidate in candidates:
            constructed_so_far.append(candidate)
            _backtrack(constructed_so_far[:], result)
            constructed_so_far.pop()

    result: list[list[int]] = []
    _backtrack([], result)
    return result


def unique_array_sum_combinations(
    array_a: list[int],
    array_b: list[int],
    array_c: list[int],
    target: int,
) -> list[tuple[int, ...]]:
    """Find unique combinations of one element per array that sum to target.

    Uses itertools.product and filters by target sum, returning only unique
    tuples.

    Args:
        array_a: First array of integers.
        array_b: Second array of integers.
        array_c: Third array of integers.
        target: The desired sum.

    Returns:
        A list of unique tuples that sum to target.

    Examples:
        >>> sorted(unique_array_sum_combinations([1, 2], [2, 3], [3, 4], 6))
        [(1, 2, 3)]
    """

    def _check_sum(expected: int, *nums: int) -> tuple[bool, tuple[int, ...]]:
        if sum(nums) == expected:
            return (True, nums)
        else:
            return (False, nums)

    product = itertools.product(array_a, array_b, array_c)
    func = partial(_check_sum, target)
    sums = list(itertools.starmap(func, product))

    seen: set[tuple[int, ...]] = set()
    for is_match, values in sums:
        if is_match and values not in seen:
            seen.add(values)

    return list(seen)

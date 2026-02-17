"""
N-Sum

Given an array of integers, find all unique n-tuples that sum to a target
value. Supports custom sum, comparison, and equality closures for advanced
use cases with non-integer elements.

Reference: https://leetcode.com/problems/4sum/

Complexity:
    Time:  O(n^(k-1)) where k is the tuple size
    Space: O(n^(k-1)) for storing results
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


def n_sum(
    n: int,
    nums: list[Any],
    target: Any,
    **kv: Callable[..., Any],
) -> list[list[Any]]:
    """Find all unique n-tuples in nums that sum to target.

    Args:
        n: Size of each tuple to find.
        nums: List of elements to search.
        target: Desired sum for each n-tuple.
        **kv: Optional closures:
            sum_closure(a, b) - returns sum of two elements.
            compare_closure(num, target) - returns -1, 0, or 1.
            same_closure(a, b) - returns True if elements are equal.

    Returns:
        Sorted list of unique n-tuples (as lists) that sum to target.

    Examples:
        >>> n_sum(3, [-1, 0, 1, 2, -1, -4], 0)
        [[-1, -1, 2], [-1, 0, 1]]
    """

    def _sum_closure_default(a: Any, b: Any) -> Any:
        return a + b

    def _compare_closure_default(num: Any, target: Any) -> int:
        if num < target:
            return -1
        elif num > target:
            return 1
        else:
            return 0

    def _same_closure_default(a: Any, b: Any) -> bool:
        return a == b

    def _n_sum_inner(n: int, nums: list[Any], target: Any) -> list[list[Any]]:
        if n == 2:
            results = _two_sum(nums, target)
        else:
            results = []
            prev_num = None
            for index, num in enumerate(nums):
                if prev_num is not None and same_closure(prev_num, num):
                    continue

                prev_num = num
                n_minus1_results = _n_sum_inner(
                    n - 1,
                    nums[index + 1 :],
                    target - num,
                )
                n_minus1_results = _append_elem_to_each_list(num, n_minus1_results)
                results += n_minus1_results
        return _union(results)

    def _two_sum(nums: list[Any], target: Any) -> list[list[Any]]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        results = []
        while left < right:
            current_sum = sum_closure(nums[left], nums[right])
            flag = compare_closure(current_sum, target)
            if flag == -1:
                left += 1
            elif flag == 1:
                right -= 1
            else:
                results.append(sorted([nums[left], nums[right]]))
                left += 1
                right -= 1
                while left < len(nums) and same_closure(nums[left - 1], nums[left]):
                    left += 1
                while right >= 0 and same_closure(nums[right], nums[right + 1]):
                    right -= 1
        return results

    def _append_elem_to_each_list(
        elem: Any, container: list[list[Any]]
    ) -> list[list[Any]]:
        results = []
        for elems in container:
            elems.append(elem)
            results.append(sorted(elems))
        return results

    def _union(
        duplicate_results: list[list[Any]],
    ) -> list[list[Any]]:
        results = []
        if len(duplicate_results) != 0:
            duplicate_results.sort()
            results.append(duplicate_results[0])
            for result in duplicate_results[1:]:
                if results[-1] != result:
                    results.append(result)
        return results

    sum_closure = kv.get("sum_closure", _sum_closure_default)
    same_closure = kv.get("same_closure", _same_closure_default)
    compare_closure = kv.get("compare_closure", _compare_closure_default)
    nums.sort()
    return _n_sum_inner(n, nums, target)

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

    sum_closure = kv.get("sum_closure", _sum_closure_default)
    same_closure = kv.get("same_closure", _same_closure_default)
    compare_closure = kv.get("compare_closure", _compare_closure_default)

    def _find_n_sum(n: int, start: int, target: Any) -> list[list[Any]]:
        results = []
        if n == 2:
            left = start
            right = len(nums) - 1
            while left < right:
                current_sum = sum_closure(nums[left], nums[right])
                flag = compare_closure(current_sum, target)
                if flag == 0:
                    results.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and same_closure(nums[left], nums[left - 1]):
                        left += 1
                    while left < right and same_closure(nums[right], nums[right + 1]):
                        right -= 1
                elif flag == -1:
                    left += 1
                else:
                    right -= 1
            return results

        for i in range(start, len(nums) - n + 1):
            if i > start and same_closure(nums[i], nums[i - 1]):
                continue
            
            # Optimization: if the smallest possible sum is greater than target, break
            # This only works for numbers/types where sum is monotonic
            # Since we have custom closures, we can't always assume this, 
            # but it's a standard optimization for the numeric case.
            
            sub_results = _find_n_sum(n - 1, i + 1, target - nums[i])
            for res in sub_results:
                results.append([nums[i]] + res)
        
        return results

    nums.sort()
    return _find_n_sum(n, 0, target)

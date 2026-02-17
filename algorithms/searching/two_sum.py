"""
Two Sum

Given a sorted array of integers and a target sum, find the 1-based indices of
the two numbers that add up to the target.  Three approaches are provided:
binary search, hash table, and two pointers.

Reference: https://en.wikipedia.org/wiki/Subset_sum_problem

Complexity:
    two_sum   -- O(n log n) time, O(1) space   (binary search)
    two_sum1  -- O(n) time, O(n) space          (hash table)
    two_sum2  -- O(n) time, O(1) space          (two pointers)
"""

from __future__ import annotations


def two_sum(numbers: list[int], target: int) -> list[int] | None:
    """Find two numbers that add up to *target* using binary search.

    Args:
        numbers: Sorted list of integers in ascending order.
        target: Desired sum of the two numbers.

    Returns:
        A list of two 1-based indices ``[i, j]`` such that
        ``numbers[i-1] + numbers[j-1] == target``, or ``None`` if no
        pair exists.

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        [1, 2]
        >>> two_sum([1, 2, 3], 7) is None
        True
    """
    for i, number in enumerate(numbers):
        second_val = target - number
        low, high = i + 1, len(numbers) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if second_val == numbers[mid]:
                return [i + 1, mid + 1]
            if second_val > numbers[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return None


def two_sum1(numbers: list[int], target: int) -> list[int] | None:
    """Find two numbers that add up to *target* using a hash table.

    Args:
        numbers: List of integers (need not be sorted).
        target: Desired sum of the two numbers.

    Returns:
        A list of two 1-based indices ``[i, j]`` such that
        ``numbers[i-1] + numbers[j-1] == target``, or ``None`` if no
        pair exists.

    Examples:
        >>> two_sum1([2, 7, 11, 15], 9)
        [1, 2]
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(numbers):
        if target - num in seen:
            return [seen[target - num] + 1, i + 1]
        seen[num] = i
    return None


def two_sum2(numbers: list[int], target: int) -> list[int] | None:
    """Find two numbers that add up to *target* using two pointers.

    Args:
        numbers: Sorted list of integers in ascending order.
        target: Desired sum of the two numbers.

    Returns:
        A list of two 1-based indices ``[i, j]`` such that
        ``numbers[i-1] + numbers[j-1] == target``, or ``None`` if no
        pair exists.

    Examples:
        >>> two_sum2([2, 7, 11, 15], 9)
        [1, 2]
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        if current_sum > target:
            right = right - 1
        else:
            left = left + 1
    return None

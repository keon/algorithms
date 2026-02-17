"""
Three Sum

Given an array of integers, find all unique triplets that sum to zero
using the two-pointer technique.

Reference: https://leetcode.com/problems/3sum/

Complexity:
    Time:  O(n^2)
    Space: O(n) for the result set
"""

from __future__ import annotations


def three_sum(array: list[int]) -> set[tuple[int, int, int]]:
    """Find all unique triplets in the array that sum to zero.

    Args:
        array: List of integers to search.

    Returns:
        Set of sorted tuples, each containing three integers summing to zero.

    Examples:
        >>> three_sum([-1, 0, 1, 2, -1, -4]) == {(-1, 0, 1), (-1, -1, 2)}
        True
    """
    result = set()
    array.sort()
    for i in range(len(array) - 2):
        if i > 0 and array[i] == array[i - 1]:
            continue
        left, right = i + 1, len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                result.add((array[i], array[left], array[right]))

                while left < right and array[left] == array[left + 1]:
                    left += 1

                while left < right and array[right] == array[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    return result

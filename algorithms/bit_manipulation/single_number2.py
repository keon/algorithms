"""
Single Number 2

Given an array of integers where every element appears three times except
for one (which appears exactly once), find that unique element using
constant space and linear time.

Reference: https://en.wikipedia.org/wiki/Exclusive_or

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def single_number2(nums: list[int]) -> int:
    """Find the element that appears once (all others appear three times).

    Uses two accumulators (*ones* and *twos*) to track bits that have
    appeared once and twice respectively; bits appearing a third time
    are cleared from both accumulators.

    Args:
        nums: A list of integers where every element except one appears
              exactly three times.

    Returns:
        The single element that appears only once.

    Examples:
        >>> single_number2([4, 2, 3, 2, 1, 1, 4, 2, 4, 1])
        3
    """
    ones, twos = 0, 0
    for index in range(len(nums)):
        ones = (ones ^ nums[index]) & ~twos
        twos = (twos ^ nums[index]) & ~ones
    return ones

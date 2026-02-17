"""
Single Number 3

Given an array where exactly two elements appear once and all others
appear exactly twice, find those two unique elements in O(n) time and
O(1) space.

Reference: https://en.wikipedia.org/wiki/Exclusive_or

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def single_number3(nums: list[int]) -> list[int]:
    """Find the two elements that each appear exactly once.

    Uses XOR to isolate the combined signature of the two unique values,
    then partitions all numbers by a distinguishing bit to separate them.

    Args:
        nums: A list of integers where exactly two elements appear once
              and all others appear exactly twice.

    Returns:
        A list containing the two unique elements.

    Examples:
        >>> sorted(single_number3([1, 2, 1, 3, 2, 5]))
        [3, 5]
    """
    xor_both = 0
    for number in nums:
        xor_both ^= number

    rightmost_set_bit = xor_both & (-xor_both)

    first, second = 0, 0
    for number in nums:
        if number & rightmost_set_bit:
            first ^= number
        else:
            second ^= number
    return [first, second]

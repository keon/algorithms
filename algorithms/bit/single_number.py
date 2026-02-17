"""
Single Number

Given an array of integers where every element appears twice except for
one, find the unique element using XOR.

Reference: https://en.wikipedia.org/wiki/Exclusive_or

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def single_number(nums: list[int]) -> int:
    """Find the element that appears only once (all others appear twice).

    XORs all values together; paired values cancel to zero, leaving the
    unique value.

    Args:
        nums: A list of integers where every element except one appears
              an even number of times.

    Returns:
        The single element, or 0 if all elements are paired.

    Examples:
        >>> single_number([1, 0, 2, 1, 2, 3, 3])
        0
        >>> single_number([101])
        101
    """
    result = 0
    for number in nums:
        result ^= number
    return result

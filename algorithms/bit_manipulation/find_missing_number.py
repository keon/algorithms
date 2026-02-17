"""
Find Missing Number

Given a sequence of unique integers in the range [0..n] with one value
missing, find and return that missing number. Two approaches are provided:
XOR-based and summation-based.

Reference: https://en.wikipedia.org/wiki/Exclusive_or

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def find_missing_number(nums: list[int]) -> int:
    """Find the missing number using XOR.

    XORs every element with its expected index so that all paired values
    cancel out, leaving only the missing number.

    Args:
        nums: A list of unique integers from 0..n with one missing.

    Returns:
        The missing integer.

    Examples:
        >>> find_missing_number([4, 1, 3, 0, 6, 5, 2])
        7
        >>> find_missing_number([0])
        1
    """
    missing = 0
    for index, number in enumerate(nums):
        missing ^= number
        missing ^= index + 1
    return missing


def find_missing_number2(nums: list[int]) -> int:
    """Find the missing number using arithmetic summation.

    Computes the expected sum of 0..n and subtracts the actual sum of
    the list to isolate the missing value.

    Args:
        nums: A list of unique integers from 0..n with one missing.

    Returns:
        The missing integer.

    Examples:
        >>> find_missing_number2([4, 1, 3, 0, 6, 5, 2])
        7
        >>> find_missing_number2([0])
        1
    """
    total = sum(nums)
    length = len(nums)
    expected_total = length * (length + 1) // 2
    return expected_total - total

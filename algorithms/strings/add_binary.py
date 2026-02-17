"""
Add Binary

Given two binary strings, return their sum as a binary string.

Reference: https://leetcode.com/problems/add-binary/

Complexity:
    Time:  O(max(m, n)) where m, n are lengths of the two strings
    Space: O(max(m, n))
"""

from __future__ import annotations


def add_binary(first: str, second: str) -> str:
    """Add two binary strings and return their binary sum.

    Args:
        first: A string representing a binary number.
        second: A string representing a binary number.

    Returns:
        A string representing the binary sum of the two inputs.

    Examples:
        >>> add_binary("11", "1")
        '100'
    """
    result = ""
    carry, index_a, index_b = 0, len(first) - 1, len(second) - 1
    zero = ord('0')
    while index_a >= 0 or index_b >= 0 or carry == 1:
        if index_a >= 0:
            carry += ord(first[index_a]) - zero
            index_a -= 1
        if index_b >= 0:
            carry += ord(second[index_b]) - zero
            index_b -= 1
        result = chr(carry % 2 + zero) + result
        carry //= 2
    return result

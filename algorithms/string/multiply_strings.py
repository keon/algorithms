"""
Multiply Strings

Given two non-negative integers represented as strings, return their product
as a string without using built-in BigInteger or direct integer conversion.

Reference: https://leetcode.com/problems/multiply-strings/

Complexity:
    Time:  O(m * n) where m, n are the lengths of the two numbers
    Space: O(m + n)
"""

from __future__ import annotations


def multiply(num1: str, num2: str) -> str:
    """Multiply two numbers represented as strings.

    Args:
        num1: The first number as a string.
        num2: The second number as a string.

    Returns:
        The product of the two numbers as a string.

    Examples:
        >>> multiply("23", "23")
        '529'
    """
    intermediate: list[int] = []
    zero = ord('0')
    position_i = 1
    for digit_i in reversed(num1):
        position_j = 1
        accumulator = 0
        for digit_j in reversed(num2):
            product = (
                (ord(digit_i) - zero)
                * (ord(digit_j) - zero)
                * position_j
                * position_i
            )
            position_j *= 10
            accumulator += product
        position_i *= 10
        intermediate.append(accumulator)
    return str(sum(intermediate))

"""
Add Bitwise Operator

Add two positive integers without using the '+' operator, using only
bitwise operations (AND, XOR, shift).

Reference: https://en.wikipedia.org/wiki/Adder_(electronics)

Complexity:
    Time:  O(log n) where n is the larger of the two inputs
    Space: O(1)
"""

from __future__ import annotations


def add_bitwise_operator(first: int, second: int) -> int:
    """Add two non-negative integers using only bitwise operations.

    Args:
        first: First non-negative integer operand.
        second: Second non-negative integer operand.

    Returns:
        The sum of first and second.

    Examples:
        >>> add_bitwise_operator(2, 3)
        5
        >>> add_bitwise_operator(0, 0)
        0
    """
    while second:
        carry = first & second
        first = first ^ second
        second = carry << 1
    return first

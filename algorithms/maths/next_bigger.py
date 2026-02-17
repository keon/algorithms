"""
Next Bigger Number with Same Digits

Given a number, find the next higher number that uses the exact same set of
digits. This is equivalent to finding the next permutation.

Reference: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

Complexity:
    Time:  O(n) where n is the number of digits
    Space: O(n)
"""

from __future__ import annotations


def next_bigger(num: int) -> int:
    """Find the next higher number with the exact same digits.

    Args:
        num: A positive integer.

    Returns:
        The next higher number with the same digits, or -1 if no such
        number exists.

    Examples:
        >>> next_bigger(38276)
        38627
        >>> next_bigger(99999)
        -1
    """
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1

    while idx >= 1 and digits[idx - 1] >= digits[idx]:
        idx -= 1

    if idx == 0:
        return -1

    pivot = digits[idx - 1]
    swap_idx = len(digits) - 1

    while pivot >= digits[swap_idx]:
        swap_idx -= 1

    digits[swap_idx], digits[idx - 1] = digits[idx - 1], digits[swap_idx]
    digits[idx:] = digits[:idx - 1:-1]

    return int(''.join(str(x) for x in digits))

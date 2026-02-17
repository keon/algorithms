"""
Plus One

Given a non-negative number represented as an array of digits (big-endian),
add one to the number and return the resulting digit array.

Reference: https://leetcode.com/problems/plus-one/

Complexity:
    Time:  O(n)
    Space: O(n) for v1, O(1) auxiliary for v2 and v3
"""

from __future__ import annotations


def plus_one_v1(digits: list[int]) -> list[int]:
    """Add one to a big-endian digit array using manual carry propagation.

    Args:
        digits: Non-empty list of digits representing a non-negative integer.

    Returns:
        New list of digits representing the input number plus one.

    Examples:
        >>> plus_one_v1([1, 2, 9])
        [1, 3, 0]
    """
    digits[-1] = digits[-1] + 1
    result = []
    carry = 0
    index = len(digits) - 1
    while index >= 0 or carry == 1:
        digit_sum = 0
        if index >= 0:
            digit_sum += digits[index]
        if carry:
            digit_sum += 1
        result.append(digit_sum % 10)
        carry = digit_sum // 10
        index -= 1
    return result[::-1]


def plus_one_v2(digits: list[int]) -> list[int]:
    """Add one to a big-endian digit array by scanning from the right.

    Args:
        digits: Non-empty list of digits representing a non-negative integer.

    Returns:
        List of digits representing the input number plus one.

    Examples:
        >>> plus_one_v2([1, 2, 9])
        [1, 3, 0]
    """
    length = len(digits)
    for index in range(length - 1, -1, -1):
        if digits[index] < 9:
            digits[index] += 1
            return digits
        digits[index] = 0
    digits.insert(0, 1)
    return digits


def plus_one_v3(num_arr: list[int]) -> list[int]:
    """Add one to a big-endian digit array using modular arithmetic.

    Args:
        num_arr: Non-empty list of digits representing a non-negative integer.

    Returns:
        List of digits representing the input number plus one.

    Examples:
        >>> plus_one_v3([1, 2, 9])
        [1, 3, 0]
    """
    for idx in reversed(list(enumerate(num_arr))):
        num_arr[idx[0]] = (num_arr[idx[0]] + 1) % 10
        if num_arr[idx[0]]:
            return num_arr
    return [1] + num_arr

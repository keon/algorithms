"""
Summing Digits Power

Find all integers in a range where each digit raised to its positional power
(1-indexed) sums to the number itself (e.g., 89 = 8^1 + 9^2).

Reference: https://en.wikipedia.org/wiki/Perfect_digit-to-digit_invariant

Complexity:
    Time:  O((high - low) * d) where d is the number of digits
    Space: O(result size)
"""

from __future__ import annotations


def sum_dig_pow(low: int, high: int) -> list[int]:
    """Find numbers where digits raised to positional powers equal the number.

    Args:
        low: Lower bound of the range (inclusive).
        high: Upper bound of the range (inclusive).

    Returns:
        List of matching numbers in the range.

    Examples:
        >>> sum_dig_pow(1, 10)
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> sum_dig_pow(1, 100)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    """
    result = []

    for number in range(low, high + 1):
        exponent = 1
        summation = 0
        number_as_string = str(number)

        tokens = list(map(int, number_as_string))

        for k in tokens:
            summation = summation + (k**exponent)
            exponent += 1

        if summation == number:
            result.append(number)
    return result

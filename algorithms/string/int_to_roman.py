"""
Integer to Roman Numeral

Given an integer, convert it to a Roman numeral string. Input is guaranteed
to be within the range from 1 to 3999.

Reference: https://en.wikipedia.org/wiki/Roman_numerals

Complexity:
    Time:  O(1) since the input range is bounded
    Space: O(1)
"""

from __future__ import annotations


def int_to_roman(num: int) -> str:
    """Convert an integer to its Roman numeral representation.

    Args:
        num: An integer between 1 and 3999.

    Returns:
        The Roman numeral string for the given integer.

    Examples:
        >>> int_to_roman(644)
        'DCXLIV'
    """
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return (
        thousands[num // 1000]
        + hundreds[(num % 1000) // 100]
        + tens[(num % 100) // 10]
        + ones[num % 10]
    )

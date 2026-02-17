"""
Roman Numeral to Integer

Given a Roman numeral string, convert it to an integer. Input is guaranteed
to be within the range from 1 to 3999.

Reference: https://en.wikipedia.org/wiki/Roman_numerals

Complexity:
    Time:  O(n) where n is the length of the Roman numeral string
    Space: O(1)
"""

from __future__ import annotations


def roman_to_int(text: str) -> int:
    """Convert a Roman numeral string to an integer.

    Args:
        text: A valid Roman numeral string.

    Returns:
        The integer value of the Roman numeral.

    Examples:
        >>> roman_to_int("DCXXI")
        621
    """
    number = 0
    roman_values = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1,
    }
    for index in range(len(text) - 1):
        if roman_values[text[index]] < roman_values[text[index + 1]]:
            number -= roman_values[text[index]]
        else:
            number += roman_values[text[index]]
    return number + roman_values[text[-1]]

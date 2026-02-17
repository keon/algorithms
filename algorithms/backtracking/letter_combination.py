"""
Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the
number could represent using a telephone keypad mapping.

Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Complexity:
    Time:  O(4^n) where n is the number of digits
    Space: O(4^n) for the result list
"""

from __future__ import annotations


def letter_combinations(digits: str) -> list[str]:
    """Return all letter combinations for a digit string.

    Args:
        digits: A string of digits (2-9).

    Returns:
        A list of all possible letter combinations.

    Examples:
        >>> letter_combinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """
    if digits == "":
        return []
    keypad_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    combinations: list[str] = [""]
    for digit in digits:
        expanded: list[str] = []
        for existing in combinations:
            for char in keypad_map[digit]:
                expanded.append(existing + char)
        combinations = expanded
    return combinations

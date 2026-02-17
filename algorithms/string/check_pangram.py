"""
Check Pangram

Checks whether a given string is a pangram, meaning it contains every
letter of the English alphabet at least once.

Reference: https://en.wikipedia.org/wiki/Pangram

Complexity:
    Time:  O(n) where n is the length of the input string
    Space: O(1)
"""

from __future__ import annotations


def check_pangram(input_string: str) -> bool:
    """Check if the input string is a pangram.

    Args:
        input_string: The string to check.

    Returns:
        True if the string contains every letter of the alphabet, False otherwise.

    Examples:
        >>> check_pangram("The quick brown fox jumps over the lazy dog")
        True
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return all(char in input_string.lower() for char in alphabet)

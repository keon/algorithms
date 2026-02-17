"""
Panagram Checker

Check whether a given string is a panagram (a sentence using every letter
of the English alphabet at least once).

Reference: https://en.wikipedia.org/wiki/Pangram

Complexity:
    Time:  O(n) where n is the length of the string
    Space: O(1) since the letter set is bounded at 26
"""

from __future__ import annotations

from string import ascii_lowercase


def panagram(string: str) -> bool:
    """Check if the input string is an English panagram.

    Args:
        string: A sentence to check.

    Returns:
        True if the string contains every English letter, False otherwise.

    Examples:
        >>> panagram("the quick brown fox jumps over the lazy dog")
        True
    """
    letters = set(ascii_lowercase)
    for char in string:
        letters.discard(char.lower())
    return len(letters) == 0

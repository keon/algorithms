"""
Anagram Checker

Given two strings, determine if they are anagrams of each other (i.e. one
can be rearranged to form the other).

Reference: https://en.wikipedia.org/wiki/Anagram

Complexity:
    Time:  O(n) where n is the length of the strings
    Space: O(1) fixed 26-character alphabet
"""

from __future__ import annotations


def anagram(first: str, second: str) -> bool:
    """Check whether two strings are anagrams of each other.

    Args:
        first: The first string (lowercase letters only).
        second: The second string (lowercase letters only).

    Returns:
        True if the strings are anagrams, False otherwise.

    Examples:
        >>> anagram('apple', 'pleap')
        True
        >>> anagram('apple', 'cherry')
        False
    """
    count_first = [0] * 26
    count_second = [0] * 26

    for char in first:
        index = ord(char) - ord("a")
        count_first[index] += 1

    for char in second:
        index = ord(char) - ord("a")
        count_second[index] += 1

    return count_first == count_second

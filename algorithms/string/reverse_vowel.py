"""
Reverse Vowels of a String

Given a string, reverse only the vowels while keeping all other characters
in their original positions.

Reference: https://leetcode.com/problems/reverse-vowels-of-a-string/

Complexity:
    Time:  O(n) where n is the length of the string
    Space: O(n) for the character list
"""

from __future__ import annotations


def reverse_vowel(text: str) -> str:
    """Reverse only the vowels in a string.

    Args:
        text: The input string.

    Returns:
        A new string with vowels reversed.

    Examples:
        >>> reverse_vowel("hello")
        'holle'
    """
    vowels = "AEIOUaeiou"
    left, right = 0, len(text) - 1
    characters = list(text)
    while left < right:
        while left < right and characters[left] not in vowels:
            left += 1
        while left < right and characters[right] not in vowels:
            right -= 1
        characters[left], characters[right] = (
            characters[right],
            characters[left],
        )
        left, right = left + 1, right - 1
    return "".join(characters)

"""
Reverse Words in a String

Given a string, reverse the order of words. Leading and trailing spaces
are trimmed and words are separated by single spaces.

Reference: https://leetcode.com/problems/reverse-words-in-a-string/

Complexity:
    Time:  O(n) where n is the length of the string
    Space: O(n)
"""

from __future__ import annotations


def _reverse_list(array: list[str], left: int, right: int) -> None:
    """Reverse a portion of a list in place.

    Args:
        array: The list to modify.
        left: The starting index.
        right: The ending index.
    """
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


def reverse_words(string: str) -> str:
    """Reverse the order of words in a string.

    Args:
        string: The input string of words.

    Returns:
        A string with the word order reversed.

    Examples:
        >>> reverse_words("I am keon kim and I like pizza")
        'pizza like I and kim keon am I'
    """
    words = string.strip().split()
    word_count = len(words)
    _reverse_list(words, 0, word_count - 1)
    return " ".join(words)

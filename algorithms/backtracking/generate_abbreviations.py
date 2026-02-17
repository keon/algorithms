"""
Generalized Abbreviations

Given a word, return all possible generalized abbreviations. Each
abbreviation replaces contiguous substrings with their lengths.

Reference: https://leetcode.com/problems/generalized-abbreviation/

Complexity:
    Time:  O(2^n) where n is the length of the word
    Space: O(n) recursion depth
"""

from __future__ import annotations


def generate_abbreviations(word: str) -> list[str]:
    """Generate all possible abbreviations of a word.

    Args:
        word: The input word to abbreviate.

    Returns:
        A list of all valid abbreviations.

    Examples:
        >>> sorted(generate_abbreviations("ab"))
        ['1b', '2', 'a1', 'ab']
    """
    result: list[str] = []
    _backtrack(result, word, 0, 0, "")
    return result


def _backtrack(
    result: list[str],
    word: str,
    position: int,
    count: int,
    current: str,
) -> None:
    """Recursively build abbreviations by including or skipping characters."""
    if position == len(word):
        if count > 0:
            current += str(count)
        result.append(current)
        return

    if count > 0:
        _backtrack(result, word, position + 1, 0,
                   current + str(count) + word[position])
    else:
        _backtrack(result, word, position + 1, 0,
                   current + word[position])
    _backtrack(result, word, position + 1, count + 1, current)

"""
Palindrome Partitioning

Given a string, find all ways to partition it into palindromic substrings.
There is always at least one way since single characters are palindromes.

Reference: https://leetcode.com/problems/palindrome-partitioning/

Complexity:
    Time:  O(n * 2^n) where n is the string length
    Space: O(n) recursion depth
"""

from __future__ import annotations

from collections.abc import Generator


def palindromic_substrings(text: str) -> list[list[str]]:
    """Return all palindrome partitions of the input string.

    Args:
        text: The string to partition.

    Returns:
        A list of partitions, each being a list of palindromic substrings.

    Examples:
        >>> palindromic_substrings("abc")
        [['a', 'b', 'c']]
    """
    if not text:
        return [[]]
    results: list[list[str]] = []
    for i in range(len(text), 0, -1):
        substring = text[:i]
        if substring == substring[::-1]:
            for rest in palindromic_substrings(text[i:]):
                results.append([substring] + rest)
    return results


def palindromic_substrings_iter(text: str) -> Generator[list[str], None, None]:
    """Yield all palindrome partitions of the input string via a generator.

    A slightly more Pythonic approach using a recursive generator.

    Args:
        text: The string to partition.

    Yields:
        Lists of palindromic substrings forming a valid partition.

    Examples:
        >>> list(palindromic_substrings_iter("abc"))
        [['a', 'b', 'c']]
    """
    if not text:
        yield []
        return
    for i in range(len(text), 0, -1):
        substring = text[:i]
        if substring == substring[::-1]:
            for rest in palindromic_substrings_iter(text[i:]):
                yield [substring] + rest

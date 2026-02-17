"""
Longest Palindromic Substring

Find the length of the longest palindromic substring using dynamic
programming with two rolling arrays.

Reference: https://en.wikipedia.org/wiki/Longest_palindromic_substring

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations


def longest_palindromic_subsequence(s: str) -> int:
    """Return the length of the longest palindromic substring in s.

    Args:
        s: The input string.

    Returns:
        Length of the longest palindromic substring.

    Examples:
        >>> longest_palindromic_subsequence("babad")
        3
        >>> longest_palindromic_subsequence("cbbd")
        2
    """
    length = len(s)
    previous_row = [0] * length
    current_row = [0] * length
    longest_length = 0

    for end in range(length):
        for start in range(end + 1):
            if end - start <= 1:
                if s[start] == s[end]:
                    current_row[start] = 1
                    span = end - start + 1
                    if longest_length < span:
                        longest_length = span
            else:
                if s[start] == s[end] and previous_row[start + 1]:
                    current_row[start] = 1
                    span = end - start + 1
                    if longest_length < span:
                        longest_length = span
        previous_row = current_row
        current_row = [0] * length

    return longest_length

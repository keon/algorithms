"""
Longest Palindromic Substring

Given a string, find the longest palindromic substring using Manacher's
algorithm, which runs in linear time.

Reference: https://en.wikipedia.org/wiki/Longest_palindromic_substring

Complexity:
    Time:  O(n) using Manacher's algorithm
    Space: O(n)
"""

from __future__ import annotations


def longest_palindrome(text: str) -> str:
    """Find the longest palindromic substring using Manacher's algorithm.

    Args:
        text: The input string to search.

    Returns:
        The longest palindromic substring.

    Examples:
        >>> longest_palindrome("cbbd")
        'bb'
    """
    if len(text) < 2:
        return text

    expanded = "#" + "#".join(text) + "#"
    palindrome_radii = [0] * len(expanded)
    center, right_boundary = 0, 0
    best_index, best_length = 0, 0

    for index in range(len(expanded)):
        if index < right_boundary and 2 * center - index < len(expanded):
            palindrome_radii[index] = min(
                right_boundary - index,
                palindrome_radii[2 * center - index],
            )
        else:
            palindrome_radii[index] = 1

        while (
            palindrome_radii[index] + index < len(expanded)
            and index - palindrome_radii[index] >= 0
            and expanded[index - palindrome_radii[index]]
            == expanded[index + palindrome_radii[index]]
        ):
            palindrome_radii[index] += 1

        if index + palindrome_radii[index] > right_boundary:
            right_boundary = index + palindrome_radii[index]
            center = index

        if palindrome_radii[index] > best_length:
            best_index = index
            best_length = palindrome_radii[index]

    substring = expanded[
        best_index - palindrome_radii[best_index] + 1 : best_index
        + palindrome_radii[best_index]
    ]
    return substring.replace("#", "")

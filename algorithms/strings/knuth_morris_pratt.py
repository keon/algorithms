"""
Knuth-Morris-Pratt String Search

Given two sequences (text and pattern), return the list of start indexes in
text that match the pattern using the KMP algorithm.

Reference: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

Complexity:
    Time:  O(n + m) where n = len(text), m = len(pattern)
    Space: O(m) for the prefix table
"""

from __future__ import annotations

from typing import List, Sequence


def knuth_morris_pratt(text: Sequence, pattern: Sequence) -> List[int]:
    """Find all occurrences of pattern in text using the KMP algorithm.

    Args:
        text: The sequence to search in.
        pattern: The pattern sequence to search for.

    Returns:
        A list of starting indices where pattern occurs in text.

    Examples:
        >>> knuth_morris_pratt('hello there hero!', 'he')
        [0, 7, 12]
    """
    text_length = len(text)
    pattern_length = len(pattern)
    prefix_table = [0 for _ in range(pattern_length)]
    match_length = 0

    for index in range(1, pattern_length):
        while match_length and pattern[index] != pattern[match_length]:
            match_length = prefix_table[match_length - 1]
        if pattern[index] == pattern[match_length]:
            match_length += 1
            prefix_table[index] = match_length

    match_length = 0
    matches: list[int] = []
    for index in range(text_length):
        while match_length and text[index] != pattern[match_length]:
            match_length = prefix_table[match_length - 1]
        if text[index] == pattern[match_length]:
            match_length += 1
            if match_length == pattern_length:
                matches.append(index - pattern_length + 1)
                match_length = prefix_table[match_length - 1]
    return matches

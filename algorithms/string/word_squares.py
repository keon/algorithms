"""
Word Squares

Given a set of words (without duplicates), find all word squares that can be
built from them. A word square reads the same horizontally and vertically.

Reference: https://leetcode.com/problems/word-squares/

Complexity:
    Time:  O(n * 26^L) where n is the number of words, L is word length
    Space: O(n * L) for the prefix map
"""

from __future__ import annotations

import collections


def word_squares(words: list[str]) -> list[list[str]]:
    """Find all valid word squares from a list of same-length words.

    Args:
        words: A list of words, all having the same length.

    Returns:
        A list of word squares, where each square is a list of words.

    Examples:
        >>> word_squares(["area", "lead", "wall", "lady", "ball"])
        [['wall', 'area', 'lead', 'lady'], ['ball', 'area', 'lead', 'lady']]
    """
    word_length = len(words[0])
    prefix_map: dict[str, list[str]] = collections.defaultdict(list)
    for word in words:
        for index in range(word_length):
            prefix_map[word[:index]].append(word)

    def _build(square: list[str]) -> None:
        if len(square) == word_length:
            squares.append(square)
            return
        prefix = ""
        for row in range(len(square)):
            prefix += square[row][len(square)]
        for word in prefix_map[prefix]:
            _build(square + [word])

    squares: list[list[str]] = []
    for word in words:
        _build([word])
    return squares

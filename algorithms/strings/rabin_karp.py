"""
Rabin-Karp String Search

A string searching algorithm that uses hashing to find a pattern in text.
Uses a rolling hash to efficiently compare the pattern hash with substrings.

Reference: https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

Complexity:
    Time:  O(n + m) average, O(n * m) worst case
    Space: O(1)
"""

from __future__ import annotations


class RollingHash:
    """A rolling hash implementation for the Rabin-Karp algorithm.

    Args:
        text: The text to compute the hash over.
        window_size: The size of the hash window.
    """

    def __init__(self, text: str, window_size: int) -> None:
        self.text = text
        self.hash = 0
        self.window_size = window_size

        for index in range(0, window_size):
            self.hash += (
                (ord(self.text[index]) - ord("a") + 1)
                * (26 ** (window_size - index - 1))
            )

        self.window_start = 0
        self.window_end = window_size

    def move_window(self) -> None:
        """Slide the hash window one position to the right."""
        if self.window_end <= len(self.text) - 1:
            self.hash -= (
                (ord(self.text[self.window_start]) - ord("a") + 1)
                * 26 ** (self.window_size - 1)
            )
            self.hash *= 26
            self.hash += ord(self.text[self.window_end]) - ord("a") + 1
            self.window_start += 1
            self.window_end += 1

    def window_text(self) -> str:
        """Return the current text within the hash window.

        Returns:
            The substring currently covered by the rolling hash window.
        """
        return self.text[self.window_start:self.window_end]


def rabin_karp(word: str, text: str) -> int | None:
    """Find the first occurrence of word in text using the Rabin-Karp algorithm.

    Args:
        word: The pattern to search for.
        text: The text to search in.

    Returns:
        The index of the first occurrence, or None if not found.

    Examples:
        >>> rabin_karp("abc", "zsnabckfkd")
        3
    """
    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return None

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for _ in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return rolling_hash.window_start
        rolling_hash.move_window()
    return None

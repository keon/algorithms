"""
Keyboard Row Filter

Given a list of words, return the words that can be typed using letters from
only one row of an American QWERTY keyboard.

Reference: https://leetcode.com/problems/keyboard-row/description/

Complexity:
    Time:  O(n * m) where n is the number of words and m is average word length
    Space: O(n)
"""

from __future__ import annotations

_KEYBOARD_ROWS: list[set[str]] = [
    set("qwertyuiop"),
    set("asdfghjkl"),
    set("zxcvbnm"),
]


def find_keyboard_row(words: list[str]) -> list[str]:
    """Return words that can be typed using one keyboard row.

    Args:
        words: A list of words to check.

    Returns:
        A list of words each typable on a single keyboard row.

    Examples:
        >>> find_keyboard_row(["Hello", "Alaska", "Dad", "Peace"])
        ['Alaska', 'Dad']
    """
    result: list[str] = []
    for word in words:
        for row in _KEYBOARD_ROWS:
            if set(word.lower()).issubset(row):
                result.append(word)
    return result

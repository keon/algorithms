"""
Make Sentence

For a given string and dictionary, count how many sentences can be formed
from the string such that all words are contained in the dictionary.

Reference: https://en.wikipedia.org/wiki/Word_break_problem

Complexity:
    Time:  O(2^n) worst case due to recursive exploration
    Space: O(n) recursion depth
"""

from __future__ import annotations

count = 0


def make_sentence(text_piece: str, dictionaries: list[str]) -> bool:
    """Check if a string can be segmented into dictionary words and count ways.

    Updates the global ``count`` variable with the number of valid segmentations.

    Args:
        text_piece: The string to segment.
        dictionaries: A list of valid dictionary words.

    Returns:
        True if any segmentation is possible (always returns True).

    Examples:
        >>> make_sentence("applet", ["", "app", "let", "t", "apple", "applet"])
        True
    """
    global count
    if len(text_piece) == 0:
        return True
    for index in range(0, len(text_piece)):
        prefix, suffix = text_piece[0:index], text_piece[index:]
        if (prefix in dictionaries
                and (suffix in dictionaries
                     or make_sentence(suffix, dictionaries))):
                count += 1
    return True

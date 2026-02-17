"""
Word Break

Given a string and a dictionary of words, determine whether the string
can be segmented into a sequence of dictionary words.

Reference: https://leetcode.com/problems/word-break/

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations


def word_break(word: str, word_dict: set[str]) -> bool:
    """Determine if word can be segmented into dictionary words.

    Args:
        word: The string to segment.
        word_dict: Set of valid dictionary words.

    Returns:
        True if word can be segmented, False otherwise.

    Examples:
        >>> word_break("leetcode", {"leet", "code"})
        True
        >>> word_break("catsandog", {"cats", "dog", "sand", "and", "cat"})
        False
    """
    dp_array = [False] * (len(word) + 1)
    dp_array[0] = True
    for i in range(1, len(word) + 1):
        for j in range(0, i):
            if dp_array[j] and word[j:i] in word_dict:
                dp_array[i] = True
                break
    return dp_array[-1]

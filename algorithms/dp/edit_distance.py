"""
Edit Distance (Levenshtein Distance)

Find the minimum number of insertions, deletions, and substitutions
required to transform one word into another.

Reference: https://en.wikipedia.org/wiki/Levenshtein_distance

Complexity:
    Time:  O(m * n)  where m, n are the lengths of the two words
    Space: O(m * n)
"""

from __future__ import annotations


def edit_distance(word_a: str, word_b: str) -> int:
    """Compute the edit distance between two words.

    Args:
        word_a: First word.
        word_b: Second word.

    Returns:
        Minimum number of single-character edits to transform word_a into word_b.

    Examples:
        >>> edit_distance('food', 'money')
        4
        >>> edit_distance('horse', 'ros')
        3
    """
    length_a, length_b = len(word_a) + 1, len(word_b) + 1

    edit = [[0 for _ in range(length_b)] for _ in range(length_a)]

    for i in range(1, length_a):
        edit[i][0] = i

    for j in range(1, length_b):
        edit[0][j] = j

    for i in range(1, length_a):
        for j in range(1, length_b):
            cost = 0 if word_a[i - 1] == word_b[j - 1] else 1
            edit[i][j] = min(
                edit[i - 1][j] + 1,
                edit[i][j - 1] + 1,
                edit[i - 1][j - 1] + cost,
            )

    return edit[-1][-1]

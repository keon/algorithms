"""
Minimum Edit Distance (Delete Operation)

Given two words, find the minimum number of steps required to make them the
same, where each step deletes one character from either string.

Reference: https://leetcode.com/problems/delete-operation-for-two-strings/

Complexity:
    Time:  O(2^n) for recursive LCS, O(m * n) for DP approach
    Space: O(m * n) for DP table
"""

from __future__ import annotations


def min_distance(word1: str, word2: str) -> int:
    """Find minimum deletions to make two words equal via recursive LCS.

    Args:
        word1: The first word.
        word2: The second word.

    Returns:
        The minimum number of deletion steps.

    Examples:
        >>> min_distance("sea", "eat")
        2
    """
    return len(word1) + len(word2) - 2 * _lcs(word1, word2, len(word1), len(word2))


def _lcs(word1: str, word2: str, length1: int, length2: int) -> int:
    """Compute the length of the longest common subsequence recursively.

    Args:
        word1: The first word.
        word2: The second word.
        length1: Current length to consider in word1.
        length2: Current length to consider in word2.

    Returns:
        The length of the longest common subsequence.
    """
    if length1 == 0 or length2 == 0:
        return 0
    if word1[length1 - 1] == word2[length2 - 1]:
        return 1 + _lcs(word1, word2, length1 - 1, length2 - 1)
    return max(
        _lcs(word1, word2, length1 - 1, length2),
        _lcs(word1, word2, length1, length2 - 1),
    )


def min_distance_dp(word1: str, word2: str) -> int:
    """Find minimum deletions to make two words equal using dynamic programming.

    Args:
        word1: The first word.
        word2: The second word.

    Returns:
        The minimum number of deletion steps.

    Examples:
        >>> min_distance_dp("sea", "eat")
        2
    """
    rows, cols = len(word1) + 1, len(word2) + 1
    table = [[0 for _ in range(cols)] for _ in range(rows)]

    if rows == cols:
        for index in range(1, rows):
            table[index][0], table[0][index] = index, index
    else:
        for index in range(rows):
            table[index][0] = index
        for index in range(cols):
            table[0][index] = index

    for row in range(1, rows):
        for col in range(1, cols):
            if word1[row - 1] == word2[col - 1]:
                table[row][col] = table[row - 1][col - 1]
            else:
                table[row][col] = min(table[row - 1][col], table[row][col - 1]) + 1

    return table[len(word1)][len(word2)]

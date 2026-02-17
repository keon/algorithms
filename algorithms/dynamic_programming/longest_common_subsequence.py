"""
Longest Common Subsequence

Find the length of the longest subsequence common to two strings.

Reference: https://en.wikipedia.org/wiki/Longest_common_subsequence

Complexity:
    Time:  O(m * n)
    Space: O(m * n)
"""

from __future__ import annotations


def longest_common_subsequence(s_1: str, s_2: str) -> int:
    """Compute the length of the longest common subsequence of two strings.

    Args:
        s_1: First string.
        s_2: Second string.

    Returns:
        Length of the longest common subsequence.

    Examples:
        >>> longest_common_subsequence('abcdgh', 'aedfhr')
        3
    """
    m = len(s_1)
    n = len(s_2)

    mat = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif s_1[i - 1] == s_2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    return mat[m][n]

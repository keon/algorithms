"""
K-Factor of a String

The K factor of a string is the number of times 'abba' appears as a
substring. Given a length and a k_factor, count the number of strings of
that length whose K factor equals k_factor.

Reference: https://en.wikipedia.org/wiki/Dynamic_programming

Complexity:
    Time:  O(length^2)
    Space: O(length^2)
"""

from __future__ import annotations


def find_k_factor(length: int, k_factor: int) -> int:
    """Count strings of given length with exactly k_factor 'abba' substrings.

    Args:
        length: Length of the strings to consider.
        k_factor: Required number of 'abba' substrings.

    Returns:
        Number of strings satisfying the K-factor constraint.

    Examples:
        >>> find_k_factor(4, 1)
        1
        >>> find_k_factor(7, 1)
        70302
    """
    mat = [
        [[0 for i in range(4)] for j in range((length - 1) // 3 + 2)]
        for k in range(length + 1)
    ]
    if 3 * k_factor + 1 > length:
        return 0

    mat[1][0][0] = 1
    mat[1][0][1] = 0
    mat[1][0][2] = 0
    mat[1][0][3] = 25

    for i in range(2, length + 1):
        for j in range((length - 1) // 3 + 2):
            if j == 0:
                mat[i][j][0] = (
                    mat[i - 1][j][0] + mat[i - 1][j][1] + mat[i - 1][j][3]
                )
                mat[i][j][1] = mat[i - 1][j][0]
                mat[i][j][2] = mat[i - 1][j][1]
                mat[i][j][3] = (
                    mat[i - 1][j][0] * 24
                    + mat[i - 1][j][1] * 24
                    + mat[i - 1][j][2] * 25
                    + mat[i - 1][j][3] * 25
                )

            elif 3 * j + 1 < i:
                mat[i][j][0] = (
                    mat[i - 1][j][0]
                    + mat[i - 1][j][1]
                    + mat[i - 1][j][3]
                    + mat[i - 1][j - 1][2]
                )
                mat[i][j][1] = mat[i - 1][j][0]
                mat[i][j][2] = mat[i - 1][j][1]
                mat[i][j][3] = (
                    mat[i - 1][j][0] * 24
                    + mat[i - 1][j][1] * 24
                    + mat[i - 1][j][2] * 25
                    + mat[i - 1][j][3] * 25
                )

            elif 3 * j + 1 == i:
                mat[i][j][0] = 1
                mat[i][j][1] = 0
                mat[i][j][2] = 0
                mat[i][j][3] = 0

            else:
                mat[i][j][0] = 0
                mat[i][j][1] = 0
                mat[i][j][2] = 0
                mat[i][j][3] = 0

    return sum(mat[length][k_factor])

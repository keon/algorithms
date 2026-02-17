"""Count paths in a grid — recursive, memoized, and bottom-up DP.

Count the number of unique paths from the top-left to the bottom-right
of an m x n grid, moving only right or down.

Inspired by PR #857 (c-cret).
"""

from __future__ import annotations

from functools import cache


def count_paths_recursive(m: int, n: int) -> int:
    """Naive recursive solution — O(2^(m+n))."""
    if m == 1 or n == 1:
        return 1
    return count_paths_recursive(m - 1, n) + count_paths_recursive(m, n - 1)


def count_paths_memo(m: int, n: int) -> int:
    """Top-down DP with memoization — O(m*n)."""

    @cache
    def helper(i: int, j: int) -> int:
        if i == 1 or j == 1:
            return 1
        return helper(i - 1, j) + helper(i, j - 1)

    return helper(m, n)


def count_paths_dp(m: int, n: int) -> int:
    """Bottom-up DP — O(m*n) time, O(n) space.

    >>> count_paths_dp(3, 7)
    28
    >>> count_paths_dp(3, 3)
    6
    """
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[n - 1]

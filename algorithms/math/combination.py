"""
Combinations (nCr)

Calculate the number of ways to choose r items from n items (binomial
coefficient) using recursive and memoized approaches.

Reference: https://en.wikipedia.org/wiki/Combination

Complexity:
    Time:  O(2^n) naive recursive, O(n*r) memoized
    Space: O(n) recursive stack, O(n*r) memoized
"""

from __future__ import annotations


def combination(n: int, r: int) -> int:
    """Calculate nCr using naive recursion.

    Args:
        n: Total number of items.
        r: Number of items to choose.

    Returns:
        The number of combinations.

    Examples:
        >>> combination(5, 2)
        10
        >>> combination(10, 5)
        252
    """
    if n == r or r == 0:
        return 1
    return combination(n - 1, r - 1) + combination(n - 1, r)


def combination_memo(n: int, r: int) -> int:
    """Calculate nCr using memoization.

    Args:
        n: Total number of items.
        r: Number of items to choose.

    Returns:
        The number of combinations.

    Examples:
        >>> combination_memo(50, 10)
        10272278170
    """
    memo: dict[tuple[int, int], int] = {}

    def _recur(n: int, r: int) -> int:
        if n == r or r == 0:
            return 1
        if (n, r) not in memo:
            memo[(n, r)] = _recur(n - 1, r - 1) + _recur(n - 1, r)
        return memo[(n, r)]

    return _recur(n, r)

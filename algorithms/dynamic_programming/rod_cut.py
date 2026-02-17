"""
Rod Cutting Problem

Given a rod of length n and a list of prices for each piece length,
determine the maximum revenue obtainable by cutting and selling the pieces.

Reference: https://en.wikipedia.org/wiki/Cutting_stock_problem

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations

_INT_MIN = -32767


def cut_rod(price: list[int]) -> int:
    """Compute the maximum obtainable value by cutting a rod optimally.

    Args:
        price: List where price[i] is the price of a piece of length i+1.

    Returns:
        Maximum revenue from cutting and selling the rod.

    Examples:
        >>> cut_rod([1, 5, 8, 9, 10, 17, 17, 20])
        22
    """
    n = len(price)
    val = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = _INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]

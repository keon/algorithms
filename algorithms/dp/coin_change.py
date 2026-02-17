"""
Coin Change (Number of Ways)

Given a value and a set of coin denominations, count how many distinct
combinations of coins sum to the given value.

Reference: https://leetcode.com/problems/coin-change-ii/

Complexity:
    Time:  O(n * m)  where n is the value and m is the number of coins
    Space: O(n)
"""

from __future__ import annotations


def count(coins: list[int], value: int) -> int:
    """Find the number of coin combinations that add up to value.

    Args:
        coins: List of coin denominations.
        value: Target sum.

    Returns:
        Number of distinct combinations that sum to value.

    Examples:
        >>> count([1, 2, 3], 4)
        4
        >>> count([2, 5, 3, 6], 10)
        5
    """
    dp_array = [1] + [0] * value

    for coin in coins:
        for i in range(coin, value + 1):
            dp_array[i] += dp_array[i - coin]

    return dp_array[value]

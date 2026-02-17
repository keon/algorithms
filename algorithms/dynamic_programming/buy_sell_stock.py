"""
Best Time to Buy and Sell Stock

Given an array of stock prices, find the maximum profit from a single
buy-sell transaction (buy before sell).

Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Complexity:
    max_profit_naive:
        Time:  O(n^2)
        Space: O(1)
    max_profit_optimized:
        Time:  O(n)
        Space: O(1)
"""

from __future__ import annotations


def max_profit_naive(prices: list[int]) -> int:
    """Find maximum profit by checking all pairs of buy/sell days.

    Args:
        prices: List of stock prices per day.

    Returns:
        Maximum achievable profit (0 if no profitable trade exists).

    Examples:
        >>> max_profit_naive([7, 1, 5, 3, 6, 4])
        5
        >>> max_profit_naive([7, 6, 4, 3, 1])
        0
    """
    max_so_far = 0
    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_so_far = max(max_so_far, prices[j] - prices[i])
    return max_so_far


def max_profit_optimized(prices: list[int]) -> int:
    """Find maximum profit using Kadane-style single pass.

    Args:
        prices: List of stock prices per day.

    Returns:
        Maximum achievable profit (0 if no profitable trade exists).

    Examples:
        >>> max_profit_optimized([7, 1, 5, 3, 6, 4])
        5
        >>> max_profit_optimized([7, 6, 4, 3, 1])
        0
    """
    cur_max, max_so_far = 0, 0
    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i - 1])
        max_so_far = max(max_so_far, cur_max)
    return max_so_far

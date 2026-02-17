"""
House Robber

Determine the maximum amount of money that can be robbed from a row of
houses without robbing two adjacent houses.

Reference: https://leetcode.com/problems/house-robber/

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def house_robber(houses: list[int]) -> int:
    """Compute the maximum robbery amount without hitting adjacent houses.

    Args:
        houses: List of non-negative integers representing money in each house.

    Returns:
        Maximum amount that can be robbed.

    Examples:
        >>> house_robber([1, 2, 16, 3, 15, 3, 12, 1])
        44
    """
    last, now = 0, 0
    for house in houses:
        last, now = now, max(last + house, now)
    return now

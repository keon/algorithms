"""
0/1 Knapsack Problem

Given items with values and weights, and a knapsack capacity, find the
maximum total value that fits in the knapsack.

Reference: https://en.wikipedia.org/wiki/Knapsack_problem

Complexity:
    Time:  O(n * m)  where n is the number of items and m is the capacity
    Space: O(m)
"""

from __future__ import annotations


class Item:
    """Represents an item with a value and weight."""

    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def get_maximum_value(items: list[Item], capacity: int) -> int:
    """Compute the maximum value achievable within the knapsack capacity.

    Args:
        items: List of Item objects with value and weight attributes.
        capacity: Maximum weight the knapsack can hold.

    Returns:
        Maximum total value that fits in the knapsack.

    Examples:
        >>> get_maximum_value([Item(60, 5), Item(50, 3), Item(70, 4), Item(30, 2)], 5)
        80
    """
    dp = [0] * (capacity + 1)
    for item in items:
        for cur_weight in reversed(range(item.weight, capacity + 1)):
            dp[cur_weight] = max(
                dp[cur_weight], item.value + dp[cur_weight - item.weight]
            )
    return dp[capacity]

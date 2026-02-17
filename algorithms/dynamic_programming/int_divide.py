"""
Integer Partition

Count the number of ways a positive integer can be represented as a sum
of positive integers (order does not matter).

Reference: https://en.wikipedia.org/wiki/Partition_(number_theory)

Complexity:
    Time:  O(n^2)
    Space: O(n^2)
"""

from __future__ import annotations


def int_divide(decompose: int) -> int:
    """Count the number of partitions of a positive integer.

    Args:
        decompose: The positive integer to partition.

    Returns:
        Number of distinct partitions.

    Examples:
        >>> int_divide(4)
        5
        >>> int_divide(7)
        15
    """
    arr = [[0 for i in range(decompose + 1)] for j in range(decompose + 1)]
    arr[1][1] = 1
    for i in range(1, decompose + 1):
        for j in range(1, decompose + 1):
            if i < j:
                arr[i][j] = arr[i][i]
            elif i == j:
                arr[i][j] = 1 + arr[i][j - 1]
            else:
                arr[i][j] = arr[i][j - 1] + arr[i - j][j]
    return arr[decompose][decompose]

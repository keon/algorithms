"""
Climbing Stairs

Count the number of distinct ways to climb a staircase of n steps,
where each move is either 1 or 2 steps.

Reference: https://leetcode.com/problems/climbing-stairs/

Complexity:
    climb_stairs:
        Time:  O(n)
        Space: O(n)
    climb_stairs_optimized:
        Time:  O(n)
        Space: O(1)
"""

from __future__ import annotations


def climb_stairs(steps: int) -> int:
    """Count distinct ways to climb n steps using a list-based DP approach.

    Args:
        steps: Number of steps in the staircase (positive integer).

    Returns:
        Number of distinct ways to reach the top.

    Examples:
        >>> climb_stairs(2)
        2
        >>> climb_stairs(10)
        89
    """
    arr = [1, 1]
    for _ in range(1, steps):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]


def climb_stairs_optimized(steps: int) -> int:
    """Count distinct ways to climb n steps using constant space.

    Args:
        steps: Number of steps in the staircase (positive integer).

    Returns:
        Number of distinct ways to reach the top.

    Examples:
        >>> climb_stairs_optimized(2)
        2
        >>> climb_stairs_optimized(10)
        89
    """
    a_steps = b_steps = 1
    for _ in range(steps):
        a_steps, b_steps = b_steps, a_steps + b_steps
    return a_steps

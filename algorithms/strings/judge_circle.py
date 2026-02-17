"""
Judge Route Circle

Given a sequence of robot moves (R, L, U, D), determine whether the robot
returns to its starting position after completing all moves.

Reference: https://leetcode.com/problems/robot-return-to-origin/

Complexity:
    Time:  O(n) where n is the number of moves
    Space: O(1)
"""

from __future__ import annotations


def judge_circle(moves: str) -> bool:
    """Determine whether a sequence of moves returns to the origin.

    Args:
        moves: A string of move characters ('U', 'D', 'L', 'R').

    Returns:
        True if the robot ends at the starting position, False otherwise.

    Examples:
        >>> judge_circle("UD")
        True
    """
    move_counts = {
        'U': 0,
        'D': 0,
        'R': 0,
        'L': 0,
    }
    for char in moves:
        move_counts[char] = move_counts[char] + 1
    return (
        move_counts['L'] == move_counts['R']
        and move_counts['U'] == move_counts['D']
    )

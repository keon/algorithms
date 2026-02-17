"""
Valid Sudoku

Determine if a partially filled 9x9 Sudoku board is valid. A board is
valid if each row, column, and 3x3 sub-box contains no duplicate digits.

Reference: https://leetcode.com/problems/valid-sudoku/

Complexity:
    Time:  O(1) (board is always 9x9)
    Space: O(1)
"""

from __future__ import annotations


def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Check whether a Sudoku board configuration is valid.

    Args:
        board: 9x9 grid where empty cells are represented by '.'.

    Returns:
        True if the board is valid, False otherwise.

    Examples:
        >>> is_valid_sudoku([['.' for _ in range(9)] for _ in range(9)])
        True
    """
    seen: list[tuple[str, ...]] = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell != ".":
                seen += [(cell, j), (i, cell), (i // 3, j // 3, cell)]
    return len(seen) == len(set(seen))

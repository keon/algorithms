"""
Sudoku Validator

Validate whether a completed 9x9 Sudoku board is a valid solution.
Each row, column, and 3x3 sub-box must contain digits 1-9 without
repetition. Boards containing zeroes are considered invalid.

Reference: https://en.wikipedia.org/wiki/Sudoku

Complexity:
    Time:  O(1)  (fixed 9x9 board)
    Space: O(1)
"""

from __future__ import annotations

from collections import defaultdict


def valid_solution_hashtable(board: list[list[int]]) -> bool:
    """Validate a Sudoku solution using hash tables.

    Args:
        board: 9x9 grid of integers (1-9 for valid, 0 for empty).

    Returns:
        True if the board is a valid Sudoku solution.

    Examples:
        >>> valid_solution_hashtable([[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]])
        True
    """
    for i in range(len(board)):
        row_seen = defaultdict(int)
        col_seen = defaultdict(int)
        for j in range(len(board[0])):
            value_row = board[i][j]
            value_col = board[j][i]
            if not value_row or value_col == 0:
                return False
            if value_row in row_seen:
                return False
            else:
                row_seen[value_row] += 1
            if value_col in col_seen:
                return False
            else:
                col_seen[value_col] += 1

    for i in range(3):
        for j in range(3):
            grid_sum = 0
            for k in range(3):
                for l in range(3):
                    grid_sum += board[i * 3 + k][j * 3 + l]
            if grid_sum != 45:
                return False
    return True


def valid_solution(board: list[list[int]]) -> bool:
    """Validate a Sudoku solution using sorted comparison.

    Args:
        board: 9x9 grid of integers (1-9 for valid, 0 for empty).

    Returns:
        True if the board is a valid Sudoku solution.

    Examples:
        >>> valid_solution([[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]])
        True
    """
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in board:
        if sorted(row) != correct:
            return False

    for column in zip(*board):
        if sorted(column) != correct:
            return False

    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i * 3:(i + 1) * 3]:
                region += line[j * 3:(j + 1) * 3]
            if sorted(region) != correct:
                return False

    return True


def valid_solution_set(board: list[list[int]]) -> bool:
    """Validate a Sudoku solution using set comparison.

    Args:
        board: 9x9 grid of integers (1-9 for valid, 0 for empty).

    Returns:
        True if the board is a valid Sudoku solution.

    Examples:
        >>> valid_solution_set([[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]])
        True
    """
    valid = set(range(1, 10))

    for row in board:
        if set(row) != valid:
            return False

    for col in [[row[i] for row in board] for i in range(9)]:
        if set(col) != valid:
            return False

    for x in range(3):
        for y in range(3):
            if set(sum([row[x * 3:(x + 1) * 3]
                        for row in board[y * 3:(y + 1) * 3]], [])) != valid:
                return False

    return True

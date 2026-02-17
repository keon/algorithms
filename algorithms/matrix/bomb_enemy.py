"""
Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
(the number zero). Return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted
point until it hits the wall since it is too strong to be destroyed.
You can only place the bomb at an empty cell.

Reference: https://leetcode.com/problems/bomb-enemy/

Complexity:
    Time:  O(m * n)
    Space: O(n)
"""

from __future__ import annotations


def max_killed_enemies(grid: list[list[str]]) -> int:
    """Return the maximum enemies killed by placing one bomb.

    Args:
        grid: 2D grid of 'W', 'E', and '0' characters.

    Returns:
        Maximum number of enemies killed.

    Examples:
        >>> max_killed_enemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])
        3
    """
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    max_killed = 0
    row_enemies, col_enemies = 0, [0] * cols
    for i in range(rows):
        for j in range(cols):
            if j == 0 or grid[i][j - 1] == 'W':
                row_enemies = _row_kills(grid, i, j)
            if i == 0 or grid[i - 1][j] == 'W':
                col_enemies[j] = _col_kills(grid, i, j)
            if grid[i][j] == '0':
                max_killed = max(max_killed, row_enemies + col_enemies[j])
    return max_killed


def _row_kills(grid: list[list[str]], row: int, col: int) -> int:
    """Count enemies killed in a row starting from the given column.

    Args:
        grid: 2D grid of characters.
        row: Row index.
        col: Starting column index.

    Returns:
        Number of enemies in the row segment.
    """
    count = 0
    num_cols = len(grid[0])
    while col < num_cols and grid[row][col] != 'W':
        if grid[row][col] == 'E':
            count += 1
        col += 1
    return count


def _col_kills(grid: list[list[str]], row: int, col: int) -> int:
    """Count enemies killed in a column starting from the given row.

    Args:
        grid: 2D grid of characters.
        row: Starting row index.
        col: Column index.

    Returns:
        Number of enemies in the column segment.
    """
    count = 0
    num_rows = len(grid)
    while row < num_rows and grid[row][col] != 'W':
        if grid[row][col] == 'E':
            count += 1
        row += 1
    return count

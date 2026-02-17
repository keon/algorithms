"""
Count Islands (DFS)

Given a 2D grid of 1s (land) and 0s (water), count the number of islands
using depth-first search.

Reference: https://leetcode.com/problems/number-of-islands/

Complexity:
    Time:  O(M * N)
    Space: O(M * N) recursion stack in worst case
"""

from __future__ import annotations


def num_islands(grid: list[list[int]]) -> int:
    """Return the number of islands in *grid*.

    Args:
        grid: 2D matrix of 0s and 1s (modified in place during traversal).

    Returns:
        Number of connected components of 1s.

    Examples:
        >>> num_islands([[1, 0], [0, 1]])
        2
    """
    count = 0
    for i in range(len(grid)):
        for j, col in enumerate(grid[i]):
            if col == 1:
                _dfs(grid, i, j)
                count += 1
    return count


def _dfs(grid: list[list[int]], i: int, j: int) -> None:
    """Flood-fill from (i, j), marking visited cells as 0.

    Args:
        grid: The grid (modified in place).
        i: Row index.
        j: Column index.
    """
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = 0
    _dfs(grid, i + 1, j)
    _dfs(grid, i - 1, j)
    _dfs(grid, i, j + 1)
    _dfs(grid, i, j - 1)

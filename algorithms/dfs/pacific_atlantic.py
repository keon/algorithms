"""
Pacific Atlantic Water Flow

Given an m*n matrix of heights, find all cells from which water can flow
to both the Pacific (top / left edges) and Atlantic (bottom / right edges)
oceans.

Reference: https://leetcode.com/problems/pacific-atlantic-water-flow/

Complexity:
    Time:  O(M * N)
    Space: O(M * N)
"""

from __future__ import annotations


def pacific_atlantic(matrix: list[list[int]]) -> list[list[int]]:
    """Return coordinates where water can flow to both oceans.

    Args:
        matrix: Height map.

    Returns:
        List of [row, col] pairs.

    Examples:
        >>> pacific_atlantic([[1]])
        [[0, 0]]
    """
    n = len(matrix)
    if not n:
        return []
    m = len(matrix[0])
    if not m:
        return []
    res: list[list[int]] = []
    atlantic = [[False for _ in range(n)] for _ in range(m)]
    pacific = [[False for _ in range(n)] for _ in range(m)]
    for i in range(n):
        _dfs(pacific, matrix, float("-inf"), i, 0)
        _dfs(atlantic, matrix, float("-inf"), i, m - 1)
    for i in range(m):
        _dfs(pacific, matrix, float("-inf"), 0, i)
        _dfs(atlantic, matrix, float("-inf"), n - 1, i)
    for i in range(n):
        for j in range(m):
            if pacific[i][j] and atlantic[i][j]:
                res.append([i, j])
    return res


def _dfs(
    grid: list[list[bool]],
    matrix: list[list[int]],
    height: float,
    i: int,
    j: int,
) -> None:
    """Mark cells reachable from (i, j) flowing uphill.

    Args:
        grid: Reachability matrix (modified in place).
        matrix: Height map.
        height: Previous cell height.
        i: Row index.
        j: Column index.
    """
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if grid[i][j] or matrix[i][j] < height:
        return
    grid[i][j] = True
    _dfs(grid, matrix, matrix[i][j], i - 1, j)
    _dfs(grid, matrix, matrix[i][j], i + 1, j)
    _dfs(grid, matrix, matrix[i][j], i, j - 1)
    _dfs(grid, matrix, matrix[i][j], i, j + 1)

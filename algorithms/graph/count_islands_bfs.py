"""
Count Islands (BFS)

Given a 2D grid of 1s (land) and 0s (water), count the number of islands
using breadth-first search.  An island is a group of adjacent lands
connected horizontally or vertically.

Reference: https://leetcode.com/problems/number-of-islands/

Complexity:
    Time:  O(M * N)
    Space: O(M * N)
"""

from __future__ import annotations


def count_islands(grid: list[list[int]]) -> int:
    """Return the number of islands in *grid*.

    Args:
        grid: 2D matrix of 0s and 1s.

    Returns:
        Number of connected components of 1s.

    Examples:
        >>> count_islands([[1, 0], [0, 1]])
        2
    """
    row = len(grid)
    col = len(grid[0])

    num_islands = 0
    visited = [[0] * col for _ in range(row)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue: list[tuple[int, int]] = []

    for i in range(row):
        for j, num in enumerate(grid[i]):
            if num == 1 and visited[i][j] != 1:
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for k in range(len(directions)):
                        nx_x = x + directions[k][0]
                        nx_y = y + directions[k][1]
                        if (0 <= nx_x < row and 0 <= nx_y < col
                                and visited[nx_x][nx_y] != 1
                                and grid[nx_x][nx_y] == 1):
                                queue.append((nx_x, nx_y))
                                visited[nx_x][nx_y] = 1
                num_islands += 1

    return num_islands

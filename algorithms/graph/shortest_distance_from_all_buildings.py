"""
Shortest Distance from All Buildings

Given a 2D grid with buildings (1), empty land (0) and obstacles (2), find
the empty land with the smallest total distance to all buildings.

Reference: https://leetcode.com/problems/shortest-distance-from-all-buildings/

Complexity:
    Time:  O(B * M * N)  where B is the number of buildings
    Space: O(M * N)
"""

from __future__ import annotations


def shortest_distance(grid: list[list[int]]) -> int:
    """Return the minimum total distance from an empty cell to all buildings.

    Args:
        grid: 2D grid (0 = empty, 1 = building, 2 = obstacle).

    Returns:
        Minimum sum of distances, or -1 if impossible.

    Examples:
        >>> shortest_distance([[1, 0, 1]])
        2
    """
    if not grid or not grid[0]:
        return -1

    matrix = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                _bfs(grid, matrix, i, j, count)
                count += 1

    res = float("inf")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j][1] == count:
                res = min(res, matrix[i][j][0])

    return res if res != float("inf") else -1


def _bfs(
    grid: list[list[int]],
    matrix: list[list[list[int]]],
    i: int,
    j: int,
    count: int,
) -> None:
    """BFS from building at (i, j), updating *matrix* distances.

    Args:
        grid: The original grid.
        matrix: Accumulator for [total_distance, visit_count].
        i: Row of the building.
        j: Column of the building.
        count: Number of buildings visited so far.
    """
    q: list[tuple[int, int, int]] = [(i, j, 0)]
    while q:
        i, j, step = q.pop(0)
        for k, col in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (
                0 <= k < len(grid)
                and 0 <= col < len(grid[0])
                and matrix[k][col][1] == count
                and grid[k][col] == 0
            ):
                matrix[k][col][0] += step + 1
                matrix[k][col][1] = count + 1
                q.append((k, col, step + 1))

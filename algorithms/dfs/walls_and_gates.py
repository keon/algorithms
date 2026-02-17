"""
Walls and Gates

Fill each empty room (INF) with the distance to its nearest gate (0).
Walls are represented by -1.

Reference: https://leetcode.com/problems/walls-and-gates/

Complexity:
    Time:  O(M * N)
    Space: O(M * N) recursion stack
"""

from __future__ import annotations


def walls_and_gates(rooms: list[list[int]]) -> None:
    """Fill *rooms* in place with distances to nearest gates.

    Args:
        rooms: 2D grid (-1 = wall, 0 = gate, INF = empty room).

    Examples:
        >>> r = [[float('inf'), 0]]; walls_and_gates(r); r
        [[1, 0]]
    """
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                _dfs(rooms, i, j, 0)


def _dfs(rooms: list[list[int]], i: int, j: int, depth: int) -> None:
    """Recursive DFS from a gate, updating room distances.

    Args:
        rooms: The grid (modified in place).
        i: Row index.
        j: Column index.
        depth: Current distance from the gate.
    """
    if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
        return
    if rooms[i][j] < depth:
        return
    rooms[i][j] = depth
    _dfs(rooms, i + 1, j, depth + 1)
    _dfs(rooms, i - 1, j, depth + 1)
    _dfs(rooms, i, j + 1, depth + 1)
    _dfs(rooms, i, j - 1, depth + 1)

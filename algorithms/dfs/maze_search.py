"""
Maze Search (DFS)

Find the shortest path from the top-left corner to the bottom-right corner
of a grid using depth-first search with backtracking.  Only cells with
value 1 may be traversed.  Returns -1 if no path exists.

Complexity:
    Time:  O(4^(M*N)) worst case (backtracking)
    Space: O(M * N)
"""

from __future__ import annotations


def find_path(maze: list[list[int]]) -> int:
    """Return the shortest path length in *maze*, or -1 if unreachable.

    Args:
        maze: 2D grid where 1 = passable, 0 = blocked.

    Returns:
        Minimum steps from (0,0) to (height-1, width-1), or -1.

    Examples:
        >>> find_path([[1, 1], [1, 1]])
        2
    """
    cnt = _dfs(maze, 0, 0, 0, -1)
    return cnt


def _dfs(
    maze: list[list[int]],
    i: int,
    j: int,
    depth: int,
    cnt: int,
) -> int:
    """Recursive DFS helper for maze search.

    Args:
        maze: The grid (modified temporarily during recursion).
        i: Current row.
        j: Current column.
        depth: Current path length.
        cnt: Best path length found so far (-1 = none).

    Returns:
        Updated best path length.
    """
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    row = len(maze)
    col = len(maze[0])

    if i == row - 1 and j == col - 1:
        if cnt == -1:
            cnt = depth
        else:
            if cnt > depth:
                cnt = depth
        return cnt

    maze[i][j] = 0

    for k in range(len(directions)):
        nx_i = i + directions[k][0]
        nx_j = j + directions[k][1]

        if 0 <= nx_i < row and 0 <= nx_j < col:
            if maze[nx_i][nx_j] == 1:
                cnt = _dfs(maze, nx_i, nx_j, depth + 1, cnt)

    maze[i][j] = 1

    return cnt

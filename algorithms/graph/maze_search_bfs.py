"""
Maze Search (BFS)

Find the minimum number of steps from the top-left corner to the
bottom-right corner of a grid.  Only cells with value 1 may be traversed.
Returns -1 if no path exists.

Complexity:
    Time:  O(M * N)
    Space: O(M * N)
"""

from __future__ import annotations

from collections import deque


def maze_search(maze: list[list[int]]) -> int:
    """Return the shortest path length in *maze*, or -1 if unreachable.

    Args:
        maze: 2D grid where 1 = passable, 0 = blocked.

    Returns:
        Minimum steps from (0,0) to (height-1, width-1), or -1.

    Examples:
        >>> maze_search([[1, 1], [1, 1]])
        2
        >>> maze_search([[1, 0], [0, 1]])
        -1
    """
    blocked, allowed = 0, 1
    unvisited, visited = 0, 1

    initial_x, initial_y = 0, 0

    if maze[initial_x][initial_y] == blocked:
        return -1

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    height, width = len(maze), len(maze[0])

    target_x, target_y = height - 1, width - 1

    queue = deque([(initial_x, initial_y, 0)])

    is_visited = [[unvisited for _ in range(width)] for _ in range(height)]
    is_visited[initial_x][initial_y] = visited

    while queue:
        x, y, steps = queue.popleft()

        if x == target_x and y == target_y:
            return steps

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < height and 0 <= new_y < width):
                continue

            if maze[new_x][new_y] == allowed and is_visited[new_x][new_y] == unvisited:
                queue.append((new_x, new_y, steps + 1))
                is_visited[new_x][new_y] = visited

    return -1

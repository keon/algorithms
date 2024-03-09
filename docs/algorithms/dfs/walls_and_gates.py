"""
You are given a m x n 2D grid initialized with these three possible values:
    -1: A wall or an obstacle.
    0: A gate.
    INF: Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF 
         as you may assume that the distance to a gate is less than 2147483647.
Fill the empty room with distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
    INF -1  0   INF
    INF INF INF -1
    INF -1  INF -1
    0   -1  INF INF
After running your function, the 2D grid should be:
    3   -1  0   1
    2   2   1   -1
    1   -1  2   -1
    0   -1  3   4
"""

def walls_and_gates(rooms):
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                dfs(rooms, i, j, 0)


def dfs(rooms, i, j, depth):
    if (i < 0 or i >= len(rooms)) or (j < 0 or j >= len(rooms[0])):
        return  # out of bounds
    if rooms[i][j] < depth:
        return  # crossed
    rooms[i][j] = depth
    dfs(rooms, i+1, j, depth+1)
    dfs(rooms, i-1, j, depth+1)
    dfs(rooms, i, j+1, depth+1)
    dfs(rooms, i, j-1, depth+1)

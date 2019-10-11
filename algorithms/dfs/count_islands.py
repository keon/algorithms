"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

def num_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j, col in enumerate(grid[i]):
            if col == 1:
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = 0
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

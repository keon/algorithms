# Given an m x n matrix of non-negative integers representing
# the height of each unit cell in a continent,
# the "Pacific ocean" touches the left and top edges of the matrix
# and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right)
# from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the
# Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

  # Pacific ~   ~   ~   ~   ~
       # ~  1   2   2   3  (5) *
       # ~  3   2   3  (4) (4) *
       # ~  2   4  (5)  3   1  *
       # ~ (6) (7)  1   4   5  *
       # ~ (5)  1   1   2   4  *
          # *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
# (positions with parentheses in above matrix).

def pacific_atlantic(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(matrix)
    if not n: return []
    m = len(matrix[0])
    if not m: return []
    res = []
    atlantic = [[False for _ in range (n)] for _ in range(m)]
    pacific =  [[False for _ in range (n)] for _ in range(m)]
    for i in range(n):
        DFS(pacific, matrix, float("-inf"), i, 0)
        DFS(atlantic, matrix, float("-inf"), i, m-1)
    for i in range(m):
        DFS(pacific, matrix, float("-inf"), 0, i)
        DFS(atlantic, matrix, float("-inf"), n-1, i)
    for i in range(n):
        for j in range(m):
            if pacific[i][j] and atlantic[i][j]:
                res.append([i, j])
    return res

def DFS(grid, matrix, height, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or  j >= len(matrix[0]):
        return
    if grid[i][j] or matrix[i][j] < height:
        return
    grid[i][j] = True
    DFS(grid, matrix, matrix[i][j], i-1, j)
    DFS(grid, matrix, matrix[i][j], i+1, j)
    DFS(grid, matrix, matrix[i][j], i, j-1)
    DFS(grid, matrix, matrix[i][j], i, j+1)

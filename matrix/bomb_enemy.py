# Given a 2D grid, each cell is either a wall 'W',
# an enemy 'E' or empty '0' (the number zero),
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from
# the planted point until it hits the wall since the wall is too strong
# to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)

def max_killed_enemies(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    max_killed = 0
    row_e, col_e = 0, [0] * n
    for i in range(m):
        for j in range(n):
            if j == 0 or grid[i][j-1] == 'W':
                row_e = row_kills(grid, i, j)

            if i == 0 or grid[i-1][j] == 'W':
                col_e[j] = col_kills(grid, i, j)

            if grid[i][j] == '0':
                max_killed = max(max_killed, row_e + col_e[j])

    return max_killed

# calculate killed enemies for row i from column j
def row_kills(grid, i, j):
    num = 0
    while j < len(grid[0]) and grid[i][j] != 'W':
        if grid[i][j] == 'E':
            num += 1
        j += 1
    return num

# calculate killed enemies for  column j from row i
def col_kills(grid, i, j):
    num = 0
    while i < len(grid) and grid[i][j] != 'W':
        if grid[i][j] == 'E':
            num += 1
        i += 1
    return num

grid = [
["0", "E", "0", "E"],
["E", "E", "E", "0"],
["E", "0", "W", "E"],
["0", "E", "0", "0"]]
print(grid)

print(max_killed_enemies(grid))


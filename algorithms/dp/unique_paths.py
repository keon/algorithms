"""

Context: we have an m*n grid (m,n are integers) and we are looking to find the amount of unique paths
we can take in order to go from the top left square to the bottom right one. We can only move one cell down
or one cell to the right each time.

"""


def unique_paths(m, n):
    # the dynamic programming matrix we are going to use in order to get the final solution
    # we initialize an m*n matrix of zeros
    dp = [[0 for _ in range(n)] for __ in range(m)]

    # dp[i][j] = the amount of unique paths we can take in order to reach the square of the grid
    # which has coordinates i and j.

    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Base case: each square in the first row and column has only 1 possible path to them

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # for each square, the amount of ways to reach it is equal to the sum of:
    #   the amount of paths we can take to the square directly above it
    #   the amount of paths we can take to the square directly to its left

    return dp[m-1][n-1]

def minCost(costMatrix, m, n, traceback=True):
    """Given a cost matrix and calculate the minimum cost path to reach (m, n) 
    from (0, 0).
    """

    tc = [[0 for x in range(m + 1)] for y in range(n + 1)]

    tc[0][0] = costMatrix[0][0]

    # Initialize first column of total cost array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + costMatrix[i][0]

    # Initialize first row of total cost array
    for i in range(1, n + 1):
        tc[0][i] = tc[0][i - 1] + costMatrix[0][i]

    # Calculate the rest of total cost array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = (
                min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + costMatrix[i][j]
            )

    path = []
    if traceback:
        path.append((m, n))

        x, y = m, n
        while x != 0 and y != 0:
            prevCost = tc[x][y] - costMatrix[x][y]

            if x > 0 and prevCost == tc[x - 1][y]:
                x -= 1
            elif y > 0 and prevCost == tc[x][y - 1]:
                y -= 1
            else:
                x -= 1
                y -= 1

            path.append((x, y))

        path.append((0, 0))

    path.reverse()
    return tc[m][n], path


# Example

costMatrix = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]

print(minCost(costMatrix, 2, 2))

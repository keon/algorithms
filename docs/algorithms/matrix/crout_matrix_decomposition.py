"""
Crout matrix decomposition is used to find two matrices that, when multiplied
give our input matrix, so L * U = A.
L stands for lower and L has non-zero elements only on diagonal and below.
U stands for upper and U has non-zero elements only on diagonal and above.

This can for example be used to solve systems of linear equations.
The last if is used  if  to avoid dividing by zero.

Example:
We input the A matrix:
[[1,2,3],
[3,4,5],
[6,7,8]]

We get:
L = [1.0,  0.0, 0.0]
    [3.0, -2.0, 0.0]
    [6.0, -5.0, 0.0]
U = [1.0,  2.0, 3.0]
    [0.0,  1.0, 2.0]
    [0.0,  0.0, 1.0]

We can check that L * U = A.

I think the complexity should be O(n^3).
"""


def crout_matrix_decomposition(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    for j in range(n):
        U[j][j] = 1.0
        for i in range(j, n):
            alpha = float(A[i][j])
            for k in range(j):
                alpha -= L[i][k]*U[k][j]
            L[i][j] = float(alpha)
        for i in range(j+1, n):
            tempU = float(A[j][i])
            for k in range(j):
                tempU -= float(L[j][k]*U[k][i])
            if int(L[j][j]) == 0:
                L[j][j] = float(0.1**40)
            U[j][i] = float(tempU/L[j][j])
    return (L, U)

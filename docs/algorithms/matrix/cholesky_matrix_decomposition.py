"""
Cholesky matrix decomposition is used to find the decomposition of a
Hermitian positive-definite matrix A
into matrix V, so that V * V* = A, where V* denotes the conjugate
transpose of L.
The dimensions of the matrix A must match.

This method is mainly used for numeric solution of linear equations Ax = b.

example:
Input matrix A:
[[  4,  12, -16],
 [ 12,  37, -43],
 [-16, -43,  98]]

Result:
[[2.0, 0.0, 0.0],
[6.0, 1.0, 0.0],
[-8.0, 5.0, 3.0]]

Time complexity of this algorithm is O(n^3), specifically about (n^3)/3

"""
import math


def cholesky_decomposition(A):
    """
    :param A: Hermitian positive-definite matrix of type List[List[float]]
    :return: matrix of type List[List[float]] if A can be decomposed,
    otherwise None
    """
    n = len(A)
    for ai in A:
        if len(ai) != n:
            return None
    V = [[0.0] * n for _ in range(n)]
    for j in range(n):
        sum_diagonal_element = 0
        for k in range(j):
            sum_diagonal_element = sum_diagonal_element + math.pow(V[j][k], 2)
        sum_diagonal_element = A[j][j] - sum_diagonal_element
        if sum_diagonal_element <= 0:
            return None
        V[j][j] = math.pow(sum_diagonal_element, 0.5)
        for i in range(j+1, n):
            sum_other_element = 0
            for k in range(j):
                sum_other_element += V[i][k]*V[j][k]
            V[i][j] = (A[i][j] - sum_other_element)/V[j][j]
    return V

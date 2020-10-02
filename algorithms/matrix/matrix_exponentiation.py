def multiply(matA: list, matB: list) -> list:
    """
    Multiplies two square matrices matA and matB od size n x n
    Time Complexity: O(n^3)
    """
    n = len(matA)
    matC = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matC[i][j] += matA[i][k] * matB[k][j]

    return matC

def identity(n: int) -> list:
    """
    Returns the Identity matrix of size n x n
    Time Complecity: O(n^2)
    """
    I = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        I[i][i] = 1
    
    return I

def matrix_exponentiation(mat: list, n: int) -> list:
    """
    Calculates mat^n by repeated squaring
    Time Complexity: O(d^3 log(n))
                     d: dimesion of the square matrix mat
                     n: power the matrix is raised to
    """
    if n == 0:
        return identity(len(mat))
    elif n % 2 == 1:
        return multiply(matrix_exponentiation(mat, n - 1), mat)
    else:
        tmp = matrix_exponentiation(mat, n // 2)
        return multiply(tmp, tmp)

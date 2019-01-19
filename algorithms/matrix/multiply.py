"""
You are given 2 matrices A and B
first it checks if the 2 martrices can be multiplied
if it can be multiplied it multiplies them in O(n^3) time
"""

def multiply(A: list,B: list)->list:
    rowsA,rowsB=len(A),len(B)
    colsA,colsB=len(A[0]),len(B[0])
    if(colsA != rowsB):
        raise Exception("Matrices cannot be multipled")

    result=[[0 for i in range(colsB)] for j in range(rowsA)]#create a result matrix
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

if __name__ == "__main__":
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]
    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
    import pprint
    pprint.pprint(multiply(A,B))

"""
kadane algorithms
Description:
    Given an m x n matrix matrix and an integer k, return 
    the max sum of a rectangle in the matrix such that its sum is no larger than k.

    It is guaranteed that there will be a rectangle with a sum 
    no larger than k.
Note:
    this algorithm is vary slow compare to others
    on worst case it takes O(n^3) time
"""
from bisect import *

def maxSumSubmatrix(matrix: list[list[int]], k:int) -> int:
    m, n = len(matrix), len(matrix[0])
    res = -float("inf")

    for l in range(n):
        rowSums = [0] * m
        for r in range(l, n):
            colSums = [0]
            colSum = 0
            for i in range(m):
                rowSums[i] += matrix[i][r]

                colSum += rowSums[i]
                diff = colSum - k
                idx = bisect_left(colSums, diff) #it will insert into the right inside the list of colSums
                # and return the index of where it added
                # we will check if the index is inside the columns

                if idx < len(colSums):
                    if colSums[idx] == diff: #if colSums is actually diff then max will be return
                        return k
                    else:
                        res = max(res, colSum - colSums[idx])
                
                # insert the "colSum" inside the "colSums" at sorted position assuming it is already sorted

    return res

    
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(f"The max sum in a matrix of {k} digits is: {maxSumSubmatrix(matrix, k)}")
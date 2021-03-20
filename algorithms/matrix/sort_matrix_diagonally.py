"""
Given a m * n matrix mat of integers,
sort it diagonally in ascending order
from the top-left to the bottom-right
then return the sorted array.

mat = [
    [3,3,1,1],
    [2,2,1,2],
    [1,1,1,2]
]

Should return:
[
    [1,1,1,1],
    [1,2,2,2],
    [1,2,3,3]
]
"""

from heapq import heappush, heappop
from typing import List


def sort_diagonally(mat: List[List[int]]) -> List[List[int]]:
    # If the input is a vector, return the vector
    if len(mat) == 1 or len(mat[0]) == 1:
        return mat

    # Rows + columns - 1
    # The -1 helps you to not repeat a column
    for i in range(len(mat)+len(mat[0])-1):
        # Process the rows
        if i+1 < len(mat):
            # Initialize heap, set row and column
            h = []
            row = len(mat)-(i+1)
            col = 0

            # Traverse diagonally, and add the values to the heap
            while row < len(mat):
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = len(mat)-(i+1)
            col = 0
            while h:
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1
        else:
            # Process the columns
            # Initialize heap, row and column
            h = []
            row = 0
            col = i - (len(mat)-1)

            # Traverse Diagonally
            while col < len(mat[0]) and row < len(mat):
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = 0
            col = i - (len(mat)-1)
            while h:
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1

    # Return the updated matrix
    return mat

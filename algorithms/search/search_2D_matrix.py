"""
Given an m x n matrix where each row is sorted in ascending order, 
and the first element of each row is greater than the last element of the previous row, 
search for a target value efficiently.

For Example:
Input: matrix = [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60]
                ], 
                target = 3
Output: True
"""
from typing import List
def searchMatrix(matrix, target):
# Edge case: if matrix is empty or has no columns
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)       # Number of rows
    n = len(matrix[0])    # Number of columns

    left = 0
    right = m * n - 1     # Treat matrix as a flattened array of size m * n

    # Binary search over the flattened 1D view
    while left <= right:
        mid = (left + right) // 2

        # Map mid index to matrix coordinates
        row = mid // n
        col = mid % n
        current_element = matrix[row][col]

        if current_element == target:
            return True  # Target found
        elif current_element < target:
            left = mid + 1  # Move right
        else:
            right = mid - 1  # Move left

    return False  # Target not found
"""
Sort Matrix Diagonally

Given an m x n matrix of integers, sort each diagonal from top-left to
bottom-right in ascending order and return the sorted matrix. Uses a
min-heap for each diagonal.

Reference: https://leetcode.com/problems/sort-the-matrix-diagonally/

Complexity:
    Time:  O((m + n) * k * log k)  where k = min(m, n)
    Space: O(min(m, n))
"""

from __future__ import annotations

from heapq import heappop, heappush


def sort_diagonally(mat: list[list[int]]) -> list[list[int]]:
    """Sort each top-left to bottom-right diagonal in ascending order.

    Args:
        mat: Matrix of size m x n.

    Returns:
        The matrix with each diagonal sorted.

    Examples:
        >>> sort_diagonally([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
        [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]
    """
    if len(mat) == 1 or len(mat[0]) == 1:
        return mat

    num_rows = len(mat)
    num_cols = len(mat[0])

    for i in range(num_rows + num_cols - 1):
        if i + 1 < num_rows:
            heap: list[int] = []
            row = num_rows - (i + 1)
            col = 0
            while row < num_rows:
                heappush(heap, mat[row][col])
                row += 1
                col += 1
            row = num_rows - (i + 1)
            col = 0
            while heap:
                mat[row][col] = heappop(heap)
                row += 1
                col += 1
        else:
            heap = []
            row = 0
            col = i - (num_rows - 1)
            while col < num_cols and row < num_rows:
                heappush(heap, mat[row][col])
                row += 1
                col += 1
            row = 0
            col = i - (num_rows - 1)
            while heap:
                mat[row][col] = heappop(heap)
                row += 1
                col += 1

    return mat

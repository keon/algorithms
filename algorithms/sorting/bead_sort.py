"""
Bead Sort

Bead sort (also known as gravity sort) simulates how beads settle under
gravity on an abacus.  It only works with non-negative integers.

Reference: https://en.wikipedia.org/wiki/Bead_sort

Complexity:
    Time:  O(n) best / O(n * max_value) average / O(n * max_value) worst
    Space: O(n * max_value)
"""

from __future__ import annotations


def bead_sort(array: list[int]) -> list[int]:
    """Sort an array of non-negative integers using bead sort.

    Args:
        array: List of non-negative integers to sort.

    Returns:
        A sorted list.

    Raises:
        ValueError: If any element is negative.

    Examples:
        >>> bead_sort([6, 3, 4, 1, 5, 2])
        [1, 2, 3, 4, 5, 6]
    """
    if any(num < 0 for num in array):
        raise ValueError("Bead sort only works with non-negative integers.")

    max_value = max(array) if array else 0
    grid = [[0] * len(array) for _ in range(max_value)]

    # Drop beads (place beads in columns)
    for col, num in enumerate(array):
        for row in range(num):
            grid[row][col] = 1

    # Let the beads "fall" (count beads in each row)
    for row in grid:
        bead_count = sum(row)
        for col in range(len(array)):
            row[col] = 1 if col < bead_count else 0

    # Read sorted values from the grid (rightmost column has fewest beads)
    n = len(array)
    sorted_array = [0] * n
    for col in range(n):
        sorted_array[col] = sum(grid[row][n - 1 - col] for row in range(max_value))
    return sorted_array

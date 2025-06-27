"""
Bead Sort (also known as Gravity Sort) is a natural sorting algorithm that simulates how beads would settle under gravity on an abacus. It is most useful for sorting positive integers, especially when the range of numbers isn't excessively large. However, it is not a comparison-based sort and is generally impractical for large inputs due to its reliance on physical modeling.
Time Complexity
- Best Case: O(n) if the numbers are already sorted
- Average Case: O(n^2) because each bead needs to be placed and then fall under gravity
- Worst Case: O(n^2) since each bead must "fall" individually
"""

def bead_sort(arr):
    if any(num < 0 for num in arr):
        raise ValueError("Bead sort only works with non-negative integers.")

    max_num = max(arr) if arr else 0
    grid = [[0] * len(arr) for _ in range(max_num)]

    # Drop beads (place beads in columns)
    for col, num in enumerate(arr):
        for row in range(num):
            grid[row][col] = 1

    # Let the beads "fall" (count beads in each row)
    for row in grid:
        sum_beads = sum(row)
        for col in range(len(arr)):
            row[col] = 1 if col < sum_beads else 0


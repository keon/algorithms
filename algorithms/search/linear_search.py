"""
Linear search works in any array.
"""


# Time Complexity O(n) and Space Complexity O(n)
def recursive_linear_search(array, index: int, target: int) -> int:
    if index < len(array):
        if array[index] == target:
            return index
        return recursive_linear_search(array, index + 1, target)
    return -1


# Time Complexity O(n) and Space Complexity O(1)
def iterative_linear_search(array, target: int) -> int:
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1

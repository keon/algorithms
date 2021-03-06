"""
Linear search works in any array.
"""


# Time Complexity O(n) and Space Complexity O(n)
def recursive_linear_search(array: list[int], index: int, target: int) -> int:
    if index < len(array):
        if array[index] == target:
            return index
        return recursive_linear_search(array, index + 1, target)
    return -1


def linear_search(array, query):
    for i in range(len(array)):
        if array[i] == query:
            return i

    return -1

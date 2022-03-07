"""
Linear search works in any array.
T(n): O(n)
"""

def linear_search(array, query):
    """
    Find the index of the given element in the array.
    There are no restrictions on the order of the elements in the array.
    If the element couldn't be found, returns -1.
    """
    for i, value in enumerate(array):
        if value == query:
            return i
    return -1

"""
Helper methods for implementing insertion sort.
"""

def search_insert(array, val):
    """
    Given a sorted array and a target value, return the index if the target is
    found. If not, return the index where it would be if it were inserted in order.

    For example:
    [1,3,5,6], 5 -> 2
    [1,3,5,6], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
    """
    for i in range(len(array)):
        if array[i] == val:
            return i
        elif array[i] > val:
            return i
    return len(array)

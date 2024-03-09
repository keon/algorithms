"""
Find last occurance of a number in a sorted array (increasing order)
Approach- Binary Search
T(n)- O(log n)
"""
def last_occurrence(array, query):
    """
    Returns the index of the last occurance of the given element in an array.
    The array has to be sorted in increasing order.
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if (array[mid] == query and mid == len(array)-1) or \
           (array[mid] == query and array[mid+1] > query):
            return mid
        if array[mid] <= query:
            low = mid + 1
        else:
            high = mid - 1

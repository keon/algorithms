"""
Find first occurance of a number in a sorted array (increasing order)
Approach- Binary Search
T(n)- O(log n)
"""
def first_occurrence(array, query):
    """
    Returns the index of the first occurance of the given element in an array.
    The array has to be sorted in increasing order.
    """

    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high-low)//2 #Now mid will be ininteger range
        #print("lo: ", lo, " hi: ", hi, " mid: ", mid)
        if low == high:
            break
        if array[mid] < query:
            low = mid + 1
        else:
            high = mid
    if array[low] == query:
        return low

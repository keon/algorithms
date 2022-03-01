"""
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element. The complexity must be O(logN)

You may assume no duplicate exists in the array.
"""
def find_min_rotate(array):
    """
    Finds the minimum element in a sorted array that has been rotated.
    """
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) // 2
        if array[mid] > array[high]:
            low = mid + 1
        else:
            high = mid

    return array[low]

def find_min_rotate_recur(array, low, high):
    """
    Finds the minimum element in a sorted array that has been rotated.
    """
    mid = (low + high) // 2
    if mid == low:
        return array[low]
    if array[mid] > array[high]:
        return find_min_rotate_recur(array, mid + 1, high)
    return find_min_rotate_recur(array, low, mid)

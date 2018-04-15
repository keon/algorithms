#
# Binary search works for a sorted array.
# Note: The code logic is written for an array sorted in
#       increasing order.
# T(n): O(log n)
#
def binary_search(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        val = array[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

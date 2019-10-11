#
# Find last occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n)- O(log n)
#
def last_occurrence(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if (array[mid] == query and mid == len(array)-1) or \
           (array[mid] == query and array[mid+1] > query):
            return mid
        elif (array[mid] <= query):
            lo = mid + 1
        else:
            hi = mid - 1

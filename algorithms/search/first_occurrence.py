#
# Find first occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n)- O(log n)
#
def first_occurrence(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        #print("lo: ", lo, " hi: ", hi, " mid: ", mid)
        if lo == hi:
            break
        if array[mid] < query:
            lo = mid + 1
        else:
            hi = mid
    if array[lo] == query:
      return lo

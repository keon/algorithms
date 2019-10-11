"""
Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

Your algorithm's runtime complexity must be in the order of O(log n).
---------------------------------------------------------------------------------
Explanation algorithm:

In classic binary search, we compare val with the midpoint to figure out if
val belongs on the low or the high side. The complication here is that the
array is rotated and may have an inflection point. Consider, for example:

Array1: [10, 15, 20, 0, 5]
Array2: [50, 5, 20, 30, 40]

Note that both arrays have a midpoint of 20, but 5 appears on the left side of
one and on the right side of the other. Therefore, comparing val with the
midpoint is insufficient.

However, if we look a bit deeper, we can see that one half of the array must be
ordered normally(increasing order). We can therefore look at the normally ordered
half to determine whether we should search the low or hight side.

For example, if we are searching for 5 in Array1, we can look at the left element (10)
and middle element (20). Since 10 < 20, the left half must be ordered normally. And, since 5
is not between those, we know that we must search the right half

In array2, we can see that since 50 > 20, the right half must be ordered normally. We turn to
the middle 20, and right 40 element to check if 5 would fall between them. The value 5 would not
Therefore, we search the left half.

There are 2 possible solution: iterative and recursion.
Recursion helps you understand better the above algorithm explanation
"""
def search_rotate(array, val):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if val == array[mid]:
            return mid

        if array[low] <= array[mid]:
            if array[low] <= val <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if array[mid] <= val <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Recursion technique
def search_rotate_recur(array, low, high, val):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if val == array[mid]:       # found element
        return mid
    if array[low] <= array[mid]:
        if array[low] <= val <= array[mid]:
            return search_rotate_recur(array, low, mid - 1, val)    # Search left
        else:
            return search_rotate_recur(array, mid + 1, high, val)   # Search right
    else:
        if array[mid] <= val <= array[high]:
            return search_rotate_recur(array, mid + 1, high, val)   # Search right
        else:
            return search_rotate_recur(array, low, mid - 1, val)    # Search left

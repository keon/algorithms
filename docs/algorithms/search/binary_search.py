"""
Binary Search

Find an element in a sorted array (in ascending order).
"""

# For Binary Search, T(N) = T(N/2) + O(1) // the recurrence relation
# Apply Masters Theorem for computing Run time complexity of recurrence relations:
#       T(N) = aT(N/b) + f(N)
# Here,
#       a = 1, b = 2 => log (a base b) = 1
# also, here
#       f(N) = n^c log^k(n)  // k = 0 & c = log (a base b)
# So,
#       T(N) = O(N^c log^(k+1)N) = O(log(N))

def binary_search(array, query):
    """
    Worst-case Complexity: O(log(n))

    reference: https://en.wikipedia.org/wiki/Binary_search_algorithm
    """

    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        if val == query:
            return mid

        if val < query:
            low = mid + 1
        else:
            high = mid - 1
    return None

#In this below function we are passing array, it's first index , last index and value to be searched
def binary_search_recur(array, low, high, val):
    """
    Worst-case Complexity: O(log(n))

    reference: https://en.wikipedia.org/wiki/Binary_search_algorithm
    """
#Here in Logic section first we are checking if low is greater than high which means its an error condition because low index should not move ahead of high index
    if low > high:       
        return -1
    mid = low + (high-low)//2   #This mid will not break integer range
    if val < array[mid]:  
        return binary_search_recur(array, low, mid - 1, val) #Go search in the left subarray
    if val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val) #Go search in the right subarray
    return mid

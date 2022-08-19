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

def binary_search_recur(array, query):
    """
    Worst-case Complexity: O(log(n))

    reference: https://en.wikipedia.org/wiki/Binary_search_algorithm
    """
    start = 0
    end = len(array)
    mid_indx = (start + end )//2
    mid_val = array[mid_indx]

    if query == mid_val:
        return mid_indx
    elif end == 1:
        return -1
    elif query > mid_val:
        temp = binary_search_recur(array[mid_indx:],query)
        if temp == -1 :return -1
        return temp + mid_indx
    else:
        return binary_search_recur(array[:mid_indx],query)

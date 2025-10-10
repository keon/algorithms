"""
This is a python implementation of the exponential search algorithm.
This algorithm is an improved version of binary search
Here instead of applying binary search on whole input we find
    an interval using exponentiation and apply binary search on it.
It is useful for unbounded/infinite lists
https://en.wikipedia.org/wiki/Exponential_search
"""


def binary_search(sequence: list, left: int, right:int, key:int) -> int:
    """
    This is a python implementation of recursive binary search algorithm.
    """
    if right >= left:
        mid = left + (right-left) // 2
        if sequence[mid] == key:
            return mid
        elif sequence[mid] > key:
            return binary_search(sequence, left, mid-1, key)
        elif sequence[mid] < key:
            return binary_search(sequence, mid+1, right, key)
    
    # Element is not present in the sequence
    return -1


def exp_search(sequence: list, key:int) -> int:
    """
    This is the exponential search method used to find the interval.
    We start with 1 and then each time multiplies it by 2 till the time
        we are in the range of our sequence and element present at start 
        of interval is less than or equal to our key.
    Be careful that the sequence must be a collection of sorted numbers, otherwise
    the algorithm will give incorrect outputs.

    Time Complexity: O(logn)
    Space Complexity: O(1)
    """
    if sequence[0] == key:
        return 0
    
    start_interval = 1
    n = len(sequence)
    
    while start_interval < n and sequence[start_interval] <= key:
        start_interval *= 2
    
    result = binary_search(sequence, start_interval // 2, min(start_interval, n-1), key)

    return result

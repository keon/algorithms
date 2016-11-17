""" 3: Sorting

    thomas moll 2015
"""

def selection_sort(arr):
    """ Selection Sort
        Complexity: O(n^2)
    """
    for i in xrange(len(arr)):
        minimum = i
        for j in xrange(i+1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j
        # Using a pythonic swap
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

def insertion_sort(arr):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    for i in xrange(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos-1]
            pos = pos-1
        # Break and do the final swap
        arr[pos] = cursor
    return arr

def merge_sort(arr):
    """ Merge Sort
        Complexity: O(n log(n))
    """
    size = len(arr)
    half = size/2
    # Our recursive base case
    if size <= 1:
        return arr
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[half:]), merge_sort(arr[:half])

    # Merge each side together
    return merge(left, right)

def merge(left, right):
    """ Merge helper
        Complexity: O(n)
    """
    arr = []
    left_cursor, right_cursor = 0,0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            arr.append(left[left_cursor])
            left_cursor+=1
        else:
            arr.append(right[right_cursor])
            right_cursor+=1
    # Add the left overs if there's any left to the result
    if left:
        arr.extend(left[left_cursor:])
    if right:
        arr.extend(right[right_cursor:])
    return arr

def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: O(n log(n))
    """
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    pivot = first
    for pos in xrange(first, last):
        if arr[pos] < arr[last]:
            arr[pos], arr[pivot] = arr[pivot], arr[pos]
            pivot += 1
    arr[pivot], arr[last] = arr[last], arr[pivot]
    return pivot

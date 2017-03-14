
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



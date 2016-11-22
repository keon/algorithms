array = [1,5, 7,4,3,2,1,9,0,10,43,64]


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

print(array)
print(quick_sort(array, 0, len(array)-1))
print(array)

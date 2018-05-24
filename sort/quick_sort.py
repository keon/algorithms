def quick_sort(arr):
    """ Quick sort
        Complexity: best O(n log(n)) avg O(n log(n)), worst O(N^2)
    """
    return quick_sort_recur(arr, 0, len(arr) - 1)


def quick_sort_recur(arr, first, last):
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        quick_sort_recur(arr, first, pos - 1)
        quick_sort_recur(arr, pos + 1, last)
    return arr


def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall

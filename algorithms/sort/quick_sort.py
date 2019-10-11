def quick_sort(arr, simulation=False):
    """ Quick sort
        Complexity: best O(n log(n)) avg O(n log(n)), worst O(N^2)
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    arr, _ = quick_sort_recur(arr, 0, len(arr) - 1, iteration, simulation)
    return arr

def quick_sort_recur(arr, first, last, iteration, simulation):
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        if simulation:
            iteration = iteration + 1
            print("iteration",iteration,":",*arr)
            
        _, iteration = quick_sort_recur(arr, first, pos - 1, iteration, simulation)
        _, iteration = quick_sort_recur(arr, pos + 1, last, iteration, simulation)

    return arr, iteration

def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall

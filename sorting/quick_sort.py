def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        print(arr[first:pos-1], arr[pos+1:last])
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    print(wall)
    return wall

array = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
print(array)
quick_sort(array, 0, len(array)-1)
print(array)

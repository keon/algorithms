def cocktail_shaker_sort(arr):
    """
    Cocktail_shaker_sort
    Sorting a given array
    mutation of bubble sort

    reference: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
    
    Worst-case performance: O(N^2)
    """

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
        if swapped == False:
            return arr
        swapped = False
        for i in range(n-1,0,-1):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr

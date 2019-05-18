def insertion_sort(arr, simulation=False):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)

    return arr

#Just a better algorithm(a better time complexity of insertion sort) added
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        for k in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = i -1
                j = j - 1

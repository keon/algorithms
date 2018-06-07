def selection_sort(arr, simulation=False):
    """ Selection Sort
        Complexity: O(n^2)
    """
    if simulation:
        print(arr)
        
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
        
        if simulation:
            print(arr)
            
    return arr

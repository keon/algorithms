def selection_sort(arr):
    """ Selection Sort
        Complexity: O(n^2)
    """
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

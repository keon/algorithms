def bitonic_sort(arr, direction):
    """
    bitonic sort is sorting algorithm to use multiple process, but this code not containing parallel process
    It can sort only array that sizes power of 2
    It can sort array in both increasing order and decreasing order by giving argument true(increasing) and false(decreasing)
    
    Worst-case in parallel: O(log(n)^2)
    Worst-case in non-parallel: O(nlog(n)^2)
    
    reference: https://en.wikipedia.org/wiki/Bitonic_sorter
    """
    n = len(arr)
    
    def compare(arr, direction):
        n = len(arr)//2
        for i in range(n):
            if direction == (arr[i] > arr[i+n]):
                arr[i], arr[i+n] = arr[i+n], arr[i]
        print(arr)
        return arr

    def bitonic_merge(arr, direction):
        n = len(arr)
        
        if n <= 1:
            return arr
        
        arr = compare(arr, direction)
        left = bitonic_merge(arr[:n // 2], direction)
        right = bitonic_merge(arr[n // 2:], direction)
        return left + right
        
    if n <= 1:
        return arr
    
    left = bitonic_sort(arr[:n // 2], True)
    right = bitonic_sort(arr[n // 2:], False)

    arr = bitonic_merge(left + right, direction)
        
    return arr

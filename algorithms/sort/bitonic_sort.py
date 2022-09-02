def bitonic_sort(arr, reverse=False):
    """
    bitonic sort is sorting algorithm to use multiple process, but this code not containing parallel process
    It can sort only array that sizes power of 2
    It can sort array in both increasing order and decreasing order by giving argument true(increasing) and false(decreasing)
    
    Worst-case in parallel: O(log(n)^2)
    Worst-case in non-parallel: O(nlog(n)^2)
    
    reference: https://en.wikipedia.org/wiki/Bitonic_sorter
    """
    def compare(arr, reverse):
        n = len(arr)//2
        for i in range(n):
            if reverse != (arr[i] > arr[i+n]):
                arr[i], arr[i+n] = arr[i+n], arr[i]
        return arr

    def bitonic_merge(arr, reverse):
        n = len(arr)
        
        if n <= 1:
            return arr
        
        arr = compare(arr, reverse)
        left = bitonic_merge(arr[:n // 2], reverse)
        right = bitonic_merge(arr[n // 2:], reverse)
        return left + right
    
    #end of function(compare and bitionic_merge) definition
    n = len(arr)
    if n <= 1:
        return arr
    # checks if n is power of two
    if not (n and (not(n & (n - 1))) ):
        raise ValueError("the size of input should be power of two")
    
    left = bitonic_sort(arr[:n // 2], True)
    right = bitonic_sort(arr[n // 2:], False)

    arr = bitonic_merge(left + right, reverse)
        
    return arr

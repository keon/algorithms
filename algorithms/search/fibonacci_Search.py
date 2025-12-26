def FibonacciSearch(arr, x):
    m = 0 
    while FibonacciGenerator(m) < len(arr): # 
        m = m + 1 
    offset = -1    
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)
        print('Current Element : ',arr[i])
        if (x > arr[i]):
            m = m - 1
            offset = i
        elif (x < arr[i]):
            m = m - 2
        else:
            return i        
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1
    return -1print('Number found at index : ',FibonacciSearch(arr, x))

def fibonacci(n):
    """
    Computes fibonacci numbers denoted F(n).
    F(0) = 0, F(1) = 1 and F(n) = F(n-1) + F(n-2) for n > 1
    
    >>>F(2)
    1
    
    >>>F(5)
    5
    
    Time Complexity : O(n)
    """
    if(n < 2):
        return n
    
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        
    return b

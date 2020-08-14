def power(a: int, n: int, r: int = None):
    """
    Iterative version of binary exponentiation
    
    Calculate a ^ n
    if r is specified, return the result modulo r
    
    Time Complexity :  O(log(n))
    Space Complexity : O(1)
    """
    ans = 1
    while n:
        if n & 1:
            ans = ans * a
        a = a * a
        if r:
            ans %= r
            a %= r
        n >>= 1
    return ans


def power_recur(a: int, n: int, r: int = None):
    """
    Recursive version of binary exponentiation
    
    Calculate a ^ n
    if r is specified, return the result modulo r
    
    Time Complexity :  O(log(n))
    Space Complexity : O(log(n))
    """
    if n == 0:
        ans = 1
    elif n == 1:
        ans = a
    else:
        ans = power_recur(a, n // 2, r)
        ans = ans * ans
        if n % 2:
            ans = ans * a
    if r:
        ans %= r
    return ans


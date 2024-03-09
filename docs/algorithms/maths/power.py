"""
Performs exponentiation, similarly to the built-in pow() or ** functions.
Allows also for calculating the exponentiation modulo.
"""
def power(a: int, n: int, mod: int = None):
    """
    Iterative version of binary exponentiation

    Calculate a ^ n
    if mod is specified, return the result modulo mod

    Time Complexity :  O(log(n))
    Space Complexity : O(1)
    """
    ans = 1
    while n:
        if n & 1:
            ans = ans * a
        a = a * a
        if mod:
            ans %= mod
            a %= mod
        n >>= 1
    return ans


def power_recur(a: int, n: int, mod: int = None):
    """
    Recursive version of binary exponentiation

    Calculate a ^ n
    if mod is specified, return the result modulo mod

    Time Complexity :  O(log(n))
    Space Complexity : O(log(n))
    """
    if n == 0:
        ans = 1
    elif n == 1:
        ans = a
    else:
        ans = power_recur(a, n // 2, mod)
        ans = ans * ans
        if n % 2:
            ans = ans * a
    if mod:
        ans %= mod
    return ans

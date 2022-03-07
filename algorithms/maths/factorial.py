"""
Calculates the factorial with the added functionality of calculating it modulo mod.
"""
def factorial(n, mod=None):
    """Calculates factorial iteratively.
    If mod is not None, then return (n! % mod)
    Time Complexity - O(n)"""
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if mod is not None and not (isinstance(mod, int) and mod > 0):
        raise ValueError("'mod' must be a positive integer")
    result = 1
    if n == 0:
        return 1
    for i in range(2, n+1):
        result *= i
        if mod:
            result %= mod
    return result


def factorial_recur(n, mod=None):
    """Calculates factorial recursively.
    If mod is not None, then return (n! % mod)
    Time Complexity - O(n)"""
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if mod is not None and not (isinstance(mod, int) and mod > 0):
        raise ValueError("'mod' must be a positive integer")
    if n == 0:
        return 1
    result = n * factorial(n - 1, mod)
    if mod:
        result %= mod
    return result

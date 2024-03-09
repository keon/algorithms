"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
the order of a modulo n is the smallest positive integer k that satisfies
pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).
Order of a certain number may or may not be exist. If not, return -1.

Total time complexity O(nlog(n)):
O(n) for iteration loop, 
O(log(n)) for built-in power function
"""

import math

def find_order(a, n):
    """
    Find order for positive integer n and given integer a that satisfies gcd(a, n) = 1.
    """
    if (a == 1) & (n == 1):
        # Exception Handeling : 1 is the order of of 1
        return 1
    if math.gcd(a, n) != 1:
        print ("a and n should be relative prime!")
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            return i
    return -1

import math

"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
the order of a modulo n is the smallest positive integer k that satisfies
pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).

"""
def findOrder(a, n):
    if (math.gcd(a, n) != 1):
        print ("a and n should be relative prime!")
        return -1
    else:
        for i in range(1, n):
            if (pow(a, i) % n == 1):
                return i
        return -1


"""
Euler's totient function, also known as phi-function ϕ(n),
counts the number of integers between 1 and n inclusive,
which are coprime to n.
(Two numbers are coprime if their greatest common divisor (GCD) equals 1).
Code from /algorithms/maths/euler_totient.py, written by 'goswami-rahul'
"""
def euler_totient(n):
    """Euler's totient function or Phi function.
    Time Complexity: O(sqrt(n))."""
    result = n;
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n;
    return result;


"""
Primitive Root
"""

def findPrimitiveRoot(n):
    phi = euler_totient(n)
    pRootList = []
    for i in range (1, n):
        if (math.gcd(i, n) != 1):
            continue
        else:
            order = findOrder(i, n)
            if (order == phi):
                pRootList.append(i)
            else:
                continue
    return pRootList

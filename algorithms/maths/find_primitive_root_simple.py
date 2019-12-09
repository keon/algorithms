import math

"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
the order of a modulo n is the smallest positive integer k that satisfies
pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).
Order of certain number may or may not be exist. If so, return -1.
"""
def find_order(a, n):
    if ((a == 1) & (n == 1)):
        return 1
        """ Exception Handeling :
        1 is the order of of 1 """
    else:
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
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
a is the primitive root of n, if a's order k for n satisfies k = ϕ(n).
Primitive roots of certain number may or may not be exist.
If so, return empty list.
"""

def find_primitive_root(n):
    if (n == 1):
        return [0]
        """ Exception Handeling :
        0 is the only primitive root of 1 """
    else:
        phi = euler_totient(n)
        p_root_list = []
        """ It will return every primitive roots of n. """
        for i in range (1, n):
            if (math.gcd(i, n) != 1):
                continue
                """ To have order, a and n must be
                relative prime with each other. """
            else:
                order = find_order(i, n)
                if (order == phi):
                    p_root_list.append(i)
                else:
                    continue
        return p_root_list

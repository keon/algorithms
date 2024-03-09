"""
Functions for calculating the greatest common divisor of two integers or
their least common multiple.
"""

def gcd(a, b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    gcd{𝑎,𝑏}=gcd{−𝑎,𝑏}=gcd{𝑎,−𝑏}=gcd{−𝑎,−𝑏}
    See proof: https://proofwiki.org/wiki/GCD_for_Negative_Integers
    """
    a_int = isinstance(a, int)
    b_int = isinstance(b, int)
    a = abs(a)
    b = abs(b)
    if not(a_int or b_int):
        raise ValueError("Input arguments are not integers")

    if (a == 0) or (b == 0) :
        raise ValueError("One or more input arguments equals zero")

    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Computes the lowest common multiple of integers a and b."""
    return abs(a) * abs(b) / gcd(a, b)

"""
Given a positive integer x, computes the number of trailing zero of x.
Example
Input : 34(100010)
           ~~~~~^
Output : 1

Input : 40(101000)
           ~~~^^^
Output : 3
"""
def trailing_zero(x):
    count = 0
    while x and not x & 1:
        count += 1
        x >>= 1
    return count

"""
Given two non-negative integer a and b,
computes the greatest common divisor of a and b using bitwise operator.
"""
def gcd_bit(a, b):
    """ Similar to gcd but uses bitwise operators and less error handling."""
    tza = trailing_zero(a)
    tzb = trailing_zero(b)
    a >>= tza
    b >>= tzb
    while b:
        if a < b:
            a, b = b, a
        a -= b
        a >>= trailing_zero(a)
    return a << min(tza, tzb)

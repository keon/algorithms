def gcd(a, b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes the lowest common multiple of integers a and b."""
    return a * b / gcd(a, b)


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
    cnt = 0
    while x and not x & 1:
        cnt += 1
        x >>= 1
    return cnt

"""
Given two non-negative integer a and b,
computes the greatest common divisor of a and b using bitwise operator.
"""

def gcd_bit(a, b):
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



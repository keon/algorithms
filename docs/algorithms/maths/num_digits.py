"""
num_digits() method will return the number of digits of a number in O(1) time using
math.log10() method.
"""

import math

def num_digits(n):
    n=abs(n)
    if n==0:
        return 1
    return int(math.log10(n))+1

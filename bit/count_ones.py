"""
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary
representation 00000000000000000000000000001011,
so the function should return 3.

T(n)- O(log n)
"""


def count_ones(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 0:
        return
    counter = 0
    while n:
        counter += n & 1
        n >>= 1
    return counter

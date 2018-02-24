"""
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary
representation 00000000000000000000000000001011,
so the function should return 3.

T(n)- O(log n)
Number of loops is
equal to the number of 1s in the binary representation."""

def count_ones(n):
    """Using Brian Kernighan’s Algorithm. (Recursive Approach)"""
    if not n: return 0
    return 1 + count_ones(n & (n-1))

def countSetBits(n):
    """Using Brian Kernighan’s Algorithm. (Iterative Approach)"""
    count = 0
    while n:
        n &= (n-1) 
        count += 1
    return count

"""
Implementation of hailstone function which generates a sequence for some n by following these rules:
* n == 1    : done
* n is even : the next n = n/2
* n is odd  : the next n = 3n + 1
"""

def hailstone(n):
    """
    Return the 'hailstone sequence' from n to 1
    n: The starting point of the hailstone sequence
    """

    sequence = [n]
    while n > 1:
        if n%2 != 0:
            n = 3*n + 1
        else:
            n = int(n/2)
        sequence.append(n)
    return sequence

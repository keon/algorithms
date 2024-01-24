''' Uses the Idea that all prime numbers are odd and for numbers like 9 we can just 
start from 3 and continously divide to eliminate 9 '''

import math
def primeFactors(n):
    res = []
    # Print the number of two's that divide n
    while n & 1 ^ 1:
        res.append(2)
        n >>= 1
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i and divide n
        while n % i == 0:
            res.append(i)
            n //= i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        res.append(n)
    return res

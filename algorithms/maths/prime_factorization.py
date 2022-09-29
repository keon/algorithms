from math import *
N = 10000001
# stores smallest prime factor for
# every number
spf = [0 for i in range(N)]
# Calculating SPF (Smallest Prime Factor)
# for every number till N.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, N):
        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i
    # separately marking spf for
    # every even number as 2
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, ceil(N ** 0.5)):
        # checking if i is prime
        if (spf[i] == i):
            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, N, i):
                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i
# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getPrimeFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
    return ret
sieve()
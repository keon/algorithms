import math
def primeFactors(N = 1000001):
    spf = [-1] * N
    for i in range(4, N, 1):
        spf[i] = 2
    for i in range(3, math.ceil(N ** 0.5)):
        if spf[i] == -1:
            for j in range(i ** 2, N, i):
                if spf[j] == -1:
                    spf[j] = i
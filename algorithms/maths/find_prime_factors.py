# Gives the shortest prime factor for a number
# Assign N the biggest num and then call getPrimeFactorization for each num
import math
N = 1000001
spf = [-1] * N
def shortesPrimeFactorForEachNum():
    global spf
    for i in range(4, N, 1):
        spf[i] = 2
    for i in range(3, math.ceil(N ** 0.5)):
        if spf[i] == -1:
            for j in range(i ** 2, N, i):
                if spf[j] == -1:
                    spf[j] = i
shortesPrimeFactorForEachNum()
def getPrimeFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
    return ret
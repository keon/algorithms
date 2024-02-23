def sieve(n = 500001):
    prime = [True for _ in range(n + 1)]
    
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for num in range(2, n + 1):
        if prime[num]: primes.append(num)

    return primes
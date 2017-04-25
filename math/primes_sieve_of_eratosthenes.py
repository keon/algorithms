'''
Using sieve of Eratosthenes, primes(x) returns list of all primes less than x
'''

def primes(x):
    assert(x>=0)
    # if you don't know the above assert function...
    # telling the program to test that condition, and trigger an error if the condition is false.
    sieve = [1 for v in range(x+1)]     # Sieve
    primes = []                         # List of Primes
    for i in range(2,x+1):
        if sieve[i]==1:
            primes.append(i)
            for j in range(i,x+1,i):
                sieve[j]=0
    return primes

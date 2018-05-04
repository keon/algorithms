'''
Using sieve of Eratosthenes, primes(x) returns list of all primes less than x

Modification:
We don't need to check all even numbers, we can make the sieve excluding even
numbers and adding 2 to the primes list by default.

We are going to make an array of: x / 2 - 1 if number is even, else x / 2 
(The -1 with even number it's to exclude the number itself)
Because we just need numbers [from 3..x if x is odd]

# We can get value represented at index i with (i*2 + 3)

For example, for x = 10, we start with an array of x / 2 - 1 = 4
[1, 1, 1, 1]
 3  5  7  9

For x = 11:
[1, 1, 1, 1, 1]
 3  5  7  9  11  # 11 is odd, it's included in the list

With this, we have reduced the array size to a half,
and complexity it's also a half now.
'''

def primes(x):
    assert(x >= 0)
    # If x is even, exclude x from list (-1):
    sieve_size = (x//2 - 1) if x % 2 == 0 else (x//2)
    sieve = [1 for v in range(sieve_size)]   # Sieve
    primes = []                              # List of Primes
    if x >= 2:
        primes.append(2)                     # Add 2 by default
    for i in range(sieve_size):
        if sieve[i] == 1:
            value_at_i = i*2 + 3
            primes.append(value_at_i)
            for j in range(i, sieve_size, value_at_i):
                sieve[j] = 0
    return primes

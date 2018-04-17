"""
Rabin-Miller primality test
returning False implies that n is guaranteed composite
returning True means that n is probably prime
with a 4 ** -k chance of being wrong
"""
import random


def is_prime(n, k):

    def pow2_factor(num):
        """factor n into a power of 2 times an odd number"""
        power = 0
        while num % 2 == 0:
            num /= 2
            power += 1
        return power, num

    def valid_witness(a):
        """
        returns true if a is a valid 'witness' for n
        a valid witness increases chances of n being prime
        an invalid witness guarantees n is composite
        """
        x = pow(int(a), int(d), int(n))

        if x == 1 or x == n - 1:
            return False

        for _ in range(r - 1):
            x = pow(int(x), int(2), int(n))

            if x == 1:
                return True
            if x == n - 1:
                return False

        return True

    # precondition n >= 5
    if n < 5:
        return n == 2 or n == 3  # True for prime

    r, d = pow2_factor(n - 1)

    for _ in range(k):
        if valid_witness(random.randrange(2, n - 2)):
            return False
    
    return True

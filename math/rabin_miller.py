import random,sys

# factor n into a power of 2 times an odd number
def pow2_factor(n):
    power = 0
    while n % 2 == 0:
        n /= 2
        power += 1
    return power, n

"""
Rabin-Miller primality test
returning False implies that n is guarenteed composite
returning True means that n is probably prime
with a 4 ** -k chance of being wrong
"""
def is_prime(n, k):
    r, d = pow2_factor(n - 1)
    
    """
    returns true if a is a valid 'witness' for n
    a valid witness increases chances of n being prime
    an invalid witness guarentees n is composite
    """
    def valid_witness(a):
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            return False
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            
            if x == 1:
                return True
            if x == n - 1:
                return False
        
        return True
    
    for _ in range(k):
        if valid_witness(random.randrange(2, n - 2)):
            return False
    
    return True
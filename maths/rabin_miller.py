import random,sys

# factor n into a power of 2 times an odd number
def pow2_factor(n):
    power = 0
    while n % 2 == 0:
        n /= 2
        power += 1
    return power, n

def pow_3(a, b, c):
    """ 
        helper function for a, b and c integers. 
    """
    return a**b % c

"""
Rabin-Miller primality test
returning False implies that n is guarenteed composite
returning True means that n is probably prime
with a 4 ** -k chance of being wrong
"""
def is_prime(n, k):
    #precondition
    assert n >= 5, "the to tested number must been >= 5"

    r, d = pow2_factor(n - 1)
    
    """
    returns true if a is a valid 'witness' for n
    a valid witness increases chances of n being prime
    an invalid witness guarentees n is composite
    """
    def valid_witness(a):
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
    
    for _ in range(k):
        if valid_witness(random.randrange(2, n - 2)):
            return False
    
    return True
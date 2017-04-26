"""
RSA encryption algorithm
a method for encrypting a number that uses seperate encryption and decryption keys
this file only implements the key generation algorithm

there are three important numbers in RSA called n, e, and d
e is called the encryption exponent
d is called the decryption exponent
n is called the modulus

these three numbers satisfy
((x ** e) ** d) % n == x % n

to use this system for encryption, n and e are made publicly available, and d is kept secret
a number x can be encrypted by computing (x ** e) % d
the original number can then be recovered by computing (E ** d) % n, where E is
the encrypted number

fortunately, python provides a three argument version of pow() that can compute powers modulo
a number very quickly:
(a ** b) % c == pow(a,b,c)
"""

import random

from rabin_miller import * # is_prime
from extended_gcd import * # extended_gcd

"""
generate a prime with k bits
"""
def genprime(k):
    while True:
        n = random.randrange(2 ** (k - 1),2 ** k)
        if is_prime(n,128):
            return n

"""
calculate the inverse of a mod m
that is, find b such that (a * b) % m == 1
"""
def modinv(a, m):
        x, y, g = extended_gcd(a,m)
        return x % m

"""
the RSA key generating algorithm
k is the number of bits in n
"""
def generate_key(k):
    # size in bits of p and q need to add up to the size of n
    p_size = k / 2
    q_size = k - p_size
    
    e = genprime(k) # in many cases, e is also chosen to be a small constant
    
    while True:
        p = genprime(k / 2)
        if p % e != 1:
            break
    
    while True:
        q = genprime(k - k / 2)
        if q % e != 1:
            break
    
    n = p * q
    l = (p - 1) * (q - 1) # calculate totient function
    d = modinv(e,l)
    
    return n, e, d

"""
sample usage:
n,e,d = generate_key(1024)
data = 1337
encrypted = pow(data,e,n)
decrypted = pow(encrypted,d,n)
assert decrypted == data
"""
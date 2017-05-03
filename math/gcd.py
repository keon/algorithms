'''
Computes gcd of integers a and b using Euclid's Algorithm
'''


def gcd(a, b):
    while True:
        if b == 0:
            return a
        a, b = b, a % b

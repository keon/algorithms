'''
Computes gcd of integers x,y using Euclid's Algorithm
'''


def gcd(x,y):
    x = abs(x)              #gcd(a,b) = gcd(|a|,b) = gcd(a,|b|) = gcd(|a|,|b|)
    y = abs(y)
    if x>y:                 # To ensure x<=y
        x,y = y,x
    if x==0:
        return y
    return gcd(y % x, x)    # Euclid's algorithm

"""
Given a positive integer N and a precision factor P,
it produces an output
with a maximum error P from the actual square root of N.

Example:
Given N = 5 and P = 0.001, can produce output x such that
2.235 < x < 2.237. Actual square root of 5 being 2.236.
"""


def square_root(n, epsilon=0.001):
    """Return square root of n, with maximum absolute error epsilon"""
    guess = n / 2

    while abs(guess * guess - n) > epsilon:
        guess = (guess + (n / guess)) / 2

    return guess

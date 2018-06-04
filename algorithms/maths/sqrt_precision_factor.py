"""
Given a positive integer N and a precision factor P,
write a square root function that produce an output
with a maximum error P from the actual square root of N.

Example:
Given N = 5 and P = 0.001, can produce output O such that
2.235 < O > 2.237. Actual square root of 5 being 2.236.
"""

def square_root(n,p):
	guess = float(n) / 2

	while abs(guess * guess - n) > p:
		guess = (guess + (n / guess)) / 2

	return guess

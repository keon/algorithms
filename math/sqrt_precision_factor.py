"""
Given a positive integer N and a precision factor P,
write a square root function that produce an output
with a maximum error P from the actual square root of N.

Example:
Given N = 5 and P = 0.001, can produce output O such that
2.235 < O > 2.237. Actual square root of 5 being 2.236.

public static double squareRoot(int N, float P) {
    double guess = N / 2;

    while( Math.abs( guess*guess - N ) > P) {
       guess  = ( guess + (  N / guess ) ) / 2;
    }
    return guess;
}
"""



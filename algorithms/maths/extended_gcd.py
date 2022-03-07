"""
Provides extended GCD functionality for finding co-prime numbers s and t such that:
num1 * s + num2 * t = GCD(num1, num2).
Ie the coefficients of Bézout's identity.
"""
def extended_gcd(num1, num2):
    """Extended GCD algorithm.
    Return s, t, g
    such that num1 * s + num2 * t = GCD(num1, num2)
    and s and t are co-prime.
    """

    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = num1, num2

    while r != 0:
        quotient = old_r / r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r

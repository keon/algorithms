def extended_gcd(a, b):
    """Extended GCD algorithm.
    Return s, t, g
    such that a * s + b * t = GCD(a, b)
    and s and t are co-prime.
    """

    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    
    while r != 0:
        quotient = old_r / r
        
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_s, old_t, old_r

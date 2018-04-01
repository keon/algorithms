def gcd(a, b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes the lowest common multiple of integers a and b."""
    return a * b / gcd(a, b)

def gcd(a, b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while True:
        if b == 0:
            return a
        a, b = b, a % b


def lcm(a, b):
    """Computes the lowest common multiple of integers a and b."""
    return a * b / gcd(a, b)

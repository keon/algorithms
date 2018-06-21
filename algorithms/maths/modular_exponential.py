def modular_exponential(base, exponent, mod):
    """Computes (base ^ exponent) % mod.
    Time complexity - O(log n)
    Use similar to Python in-built function pow."""
    if exponent < 0:
        raise ValueError("Exponent must be positive.")
    base %= mod
    result = 1

    while exponent > 0:
        # If the last bit is 1, add 2^k.
        if exponent & 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        # Utilize modular multiplication properties to combine the computed mod C values.
        base = (base * base) % mod

    return result

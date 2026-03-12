"""
RSA Encryption Algorithm

Implements RSA key generation, encryption, and decryption. RSA uses separate
public and private keys where ((x^e)^d) % n == x % n.

Reference: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

Complexity:
    Time:  O(k^3) for key generation (k = bit length)
    Space: O(k)
"""

from __future__ import annotations

import secrets


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def _modinv(a: int, m: int) -> int:
    g, x, _ = _extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse does not exist: gcd({a}, {m}) = {g}")
    return x % m


def generate_key(k: int, seed: int | None = None) -> tuple[int, int, int]:
    """Generate an RSA key triplet (n, e, d).

    Args:
        k: The number of bits in the modulus n.
        seed: Optional random seed for reproducibility (ignored, kept for API compatibility).

    Returns:
        A tuple (n, e, d) where n is the modulus, e is the encryption
        exponent, and d is the decryption exponent.

    Examples:
        >>> n, e, d = generate_key(16)
    """

    def _gen_prime(k: int, seed: int | None = None) -> int:
        """Generate a random prime with k bits.

        Args:
            k: The number of bits.
            seed: Unused, kept for API compatibility.

        Returns:
            A prime number.
        """

        def _is_prime(num: int) -> bool:
            if num == 2:
                return True
            return all(
                num % i != 0
                for i in range(2, int(num**0.5) + 1)
            )

        while True:
            key = secrets.randbelow(int(2**k) - int(2 ** (k - 1))) + int(2 ** (k - 1))
            if _is_prime(key):
                return key

    p_size = k // 2
    q_size = k - p_size

    e = _gen_prime(k, seed)

    while True:
        p = _gen_prime(p_size, seed)
        if p % e != 1:
            break

    while True:
        q = _gen_prime(q_size, seed)
        if q % e != 1:
            break

    n = p * q
    totient = (p - 1) * (q - 1)
    d = _modinv(e, totient)

    return int(n), int(e), int(d)


def encrypt(data: int, e: int, n: int) -> int:
    """Encrypt data using RSA public key.

    Args:
        data: The plaintext integer.
        e: The encryption exponent.
        n: The modulus.

    Returns:
        The encrypted integer.

    Examples:
        >>> encrypt(7, 23, 143)
        2
    """
    return pow(int(data), int(e), int(n))


def decrypt(data: int, d: int, n: int) -> int:
    """Decrypt data using RSA private key.

    Args:
        data: The encrypted integer.
        d: The decryption exponent.
        n: The modulus.

    Returns:
        The decrypted plaintext integer.

    Examples:
        >>> decrypt(2, 47, 143)
        7
    """
    return pow(int(data), int(d), int(n))

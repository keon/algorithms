"""
Diffie-Hellman Key Exchange

Implements the Diffie-Hellman key exchange protocol, which enables two parties
to establish a shared secret over an insecure channel using discrete
logarithm properties.

Reference: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

Complexity:
    Time:  O(p) for primitive root finding, O(log(p)) for key generation
    Space: O(p) for primitive root list
"""

from __future__ import annotations

import math
from random import randint


def _prime_check(num: int) -> bool:
    """Check whether a number is prime.

    Args:
        num: The integer to test.

    Returns:
        True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    j = 5
    while j * j <= num:
        if num % j == 0 or num % (j + 2) == 0:
            return False
        j += 6
    return True


def _find_order(a: int, n: int) -> int:
    """Find the multiplicative order of a modulo n.

    Args:
        a: The base integer.
        n: The modulus.

    Returns:
        The smallest positive k such that a^k = 1 (mod n), or -1 if none exists.
    """
    if (a == 1) & (n == 1):
        return 1
    if math.gcd(a, n) != 1:
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            return i
    return -1


def _euler_totient(n: int) -> int:
    """Compute Euler's totient function phi(n).

    Args:
        n: A positive integer.

    Returns:
        The number of integers from 1 to n that are coprime with n.
    """
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result


def _find_primitive_root(n: int) -> list[int]:
    """Find all primitive roots of n.

    Args:
        n: A positive integer.

    Returns:
        List of all primitive roots of n, or empty list if none exist.
    """
    if n == 1:
        return [0]
    phi = _euler_totient(n)
    p_root_list = []
    for i in range(1, n):
        if math.gcd(i, n) != 1:
            continue
        order = _find_order(i, n)
        if order == phi:
            p_root_list.append(i)
    return p_root_list


def alice_private_key(p: int) -> int:
    """Generate Alice's private key in range [1, p-1].

    Args:
        p: A large prime number.

    Returns:
        A random private key.
    """
    return randint(1, p - 1)


def alice_public_key(a_pr_k: int, a: int, p: int) -> int:
    """Calculate Alice's public key.

    Args:
        a_pr_k: Alice's private key.
        a: The primitive root (generator).
        p: The prime modulus.

    Returns:
        Alice's public key.
    """
    return pow(a, a_pr_k) % p


def bob_private_key(p: int) -> int:
    """Generate Bob's private key in range [1, p-1].

    Args:
        p: A large prime number.

    Returns:
        A random private key.
    """
    return randint(1, p - 1)


def bob_public_key(b_pr_k: int, a: int, p: int) -> int:
    """Calculate Bob's public key.

    Args:
        b_pr_k: Bob's private key.
        a: The primitive root (generator).
        p: The prime modulus.

    Returns:
        Bob's public key.
    """
    return pow(a, b_pr_k) % p


def alice_shared_key(b_pu_k: int, a_pr_k: int, p: int) -> int:
    """Calculate Alice's shared secret key.

    Args:
        b_pu_k: Bob's public key.
        a_pr_k: Alice's private key.
        p: The prime modulus.

    Returns:
        The shared secret key.
    """
    return pow(b_pu_k, a_pr_k) % p


def bob_shared_key(a_pu_k: int, b_pr_k: int, p: int) -> int:
    """Calculate Bob's shared secret key.

    Args:
        a_pu_k: Alice's public key.
        b_pr_k: Bob's private key.
        p: The prime modulus.

    Returns:
        The shared secret key.
    """
    return pow(a_pu_k, b_pr_k) % p


def diffie_hellman_key_exchange(a: int, p: int, option: int | None = None) -> bool:
    """Perform Diffie-Hellman key exchange and verify shared keys match.

    Args:
        a: The primitive root (generator).
        p: A large prime number.
        option: Unused, kept for API compatibility.

    Returns:
        True if both parties compute the same shared key, False if
        inputs are invalid.

    Examples:
        >>> diffie_hellman_key_exchange(3, 353)
        True
    """
    if _prime_check(p) is False:
        return False
    try:
        p_root_list = _find_primitive_root(p)
        p_root_list.index(a)
    except ValueError:
        return False

    a_pr_k = alice_private_key(p)
    a_pu_k = alice_public_key(a_pr_k, a, p)

    b_pr_k = bob_private_key(p)
    b_pu_k = bob_public_key(b_pr_k, a, p)

    a_sh_k = alice_shared_key(b_pu_k, a_pr_k, p)
    b_sh_k = bob_shared_key(a_pu_k, b_pr_k, p)

    return a_sh_k == b_sh_k

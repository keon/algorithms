"""
Collection of mathematical algorithms and functions.
"""

from __future__ import annotations

# Module-level imports for backward compatibility (tests use module.function syntax)
from algorithms.math import (
    chinese_remainder_theorem,  # noqa: E402
    fft,  # noqa: E402
    hailstone,  # noqa: E402
    modular_inverse,  # type: ignore[no-redef]  # noqa: E402
)
from algorithms.math.base_conversion import base_to_int, int_to_base
from algorithms.math.combination import combination, combination_memo
from algorithms.math.cosine_similarity import cosine_similarity
from algorithms.math.decimal_to_binary_ip import (
    decimal_to_binary_ip,
    decimal_to_binary_util,
)
from algorithms.math.diffie_hellman_key_exchange import (
    alice_private_key,
    alice_public_key,
    alice_shared_key,
    bob_private_key,
    bob_public_key,
    bob_shared_key,
    diffie_hellman_key_exchange,
)
from algorithms.math.distance_between_two_points import distance_between_two_points
from algorithms.math.euler_totient import euler_totient
from algorithms.math.extended_gcd import extended_gcd
from algorithms.math.factorial import factorial, factorial_recur
from algorithms.math.find_order_simple import find_order
from algorithms.math.find_primitive_root_simple import find_primitive_root
from algorithms.math.gcd import gcd, gcd_bit, lcm, trailing_zero
from algorithms.math.generate_strobogrammtic import (
    gen_strobogrammatic,
    strobogrammatic_in_range,
)
from algorithms.math.is_strobogrammatic import is_strobogrammatic, is_strobogrammatic2
from algorithms.math.krishnamurthy_number import krishnamurthy_number
from algorithms.math.magic_number import magic_number
from algorithms.math.modular_exponential import modular_exponential
from algorithms.math.next_bigger import next_bigger
from algorithms.math.next_perfect_square import find_next_square, find_next_square2
from algorithms.math.nth_digit import find_nth_digit
from algorithms.math.num_digits import num_digits
from algorithms.math.num_perfect_squares import num_perfect_squares
from algorithms.math.power import power, power_recur
from algorithms.math.prime_check import prime_check
from algorithms.math.primes_sieve_of_eratosthenes import get_primes
from algorithms.math.pythagoras import pythagoras
from algorithms.math.rabin_miller import is_prime
from algorithms.math.recursive_binomial_coefficient import (
    recursive_binomial_coefficient,
)
from algorithms.math.rsa import decrypt, encrypt, generate_key
from algorithms.math.sqrt_precision_factor import square_root
from algorithms.math.summing_digits import sum_dig_pow
from algorithms.math.surface_area_of_torus import surface_area_of_torus

__all__ = [
    "base_to_int",
    "int_to_base",
    "chinese_remainder_theorem",
    "combination",
    "combination_memo",
    "cosine_similarity",
    "decimal_to_binary_ip",
    "decimal_to_binary_util",
    "alice_private_key",
    "alice_public_key",
    "alice_shared_key",
    "bob_private_key",
    "bob_public_key",
    "bob_shared_key",
    "diffie_hellman_key_exchange",
    "distance_between_two_points",
    "euler_totient",
    "extended_gcd",
    "factorial",
    "factorial_recur",
    "fft",
    "find_order",
    "find_primitive_root",
    "gcd",
    "gcd_bit",
    "lcm",
    "trailing_zero",
    "gen_strobogrammatic",
    "strobogrammatic_in_range",
    "hailstone",
    "is_strobogrammatic",
    "is_strobogrammatic2",
    "krishnamurthy_number",
    "magic_number",
    "modular_exponential",
    "modular_inverse",
    "next_bigger",
    "find_next_square",
    "find_next_square2",
    "find_nth_digit",
    "num_digits",
    "num_perfect_squares",
    "power",
    "power_recur",
    "prime_check",
    "get_primes",
    "pythagoras",
    "is_prime",
    "recursive_binomial_coefficient",
    "decrypt",
    "encrypt",
    "generate_key",
    "square_root",
    "sum_dig_pow",
    "surface_area_of_torus",
]

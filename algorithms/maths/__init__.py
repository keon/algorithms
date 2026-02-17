"""
Collection of mathematical algorithms and functions.
"""

from __future__ import annotations

from algorithms.maths.base_conversion import base_to_int, int_to_base
from algorithms.maths.combination import combination, combination_memo
from algorithms.maths.cosine_similarity import cosine_similarity
from algorithms.maths.decimal_to_binary_ip import (
    decimal_to_binary_ip,
    decimal_to_binary_util,
)
from algorithms.maths.diffie_hellman_key_exchange import (
    alice_private_key,
    alice_public_key,
    alice_shared_key,
    bob_private_key,
    bob_public_key,
    bob_shared_key,
    diffie_hellman_key_exchange,
)
from algorithms.maths.distance_between_two_points import distance_between_two_points
from algorithms.maths.euler_totient import euler_totient
from algorithms.maths.extended_gcd import extended_gcd
from algorithms.maths.factorial import factorial, factorial_recur
from algorithms.maths.find_order_simple import find_order
from algorithms.maths.find_primitive_root_simple import find_primitive_root
from algorithms.maths.gcd import gcd, gcd_bit, lcm, trailing_zero
from algorithms.maths.generate_strobogrammtic import (
    gen_strobogrammatic,
    strobogrammatic_in_range,
)
from algorithms.maths.is_strobogrammatic import is_strobogrammatic, is_strobogrammatic2
from algorithms.maths.krishnamurthy_number import krishnamurthy_number
from algorithms.maths.magic_number import magic_number
from algorithms.maths.modular_exponential import modular_exponential
from algorithms.maths.next_bigger import next_bigger
from algorithms.maths.next_perfect_square import find_next_square, find_next_square2
from algorithms.maths.nth_digit import find_nth_digit
from algorithms.maths.num_digits import num_digits
from algorithms.maths.num_perfect_squares import num_perfect_squares
from algorithms.maths.power import power, power_recur
from algorithms.maths.prime_check import prime_check
from algorithms.maths.primes_sieve_of_eratosthenes import get_primes
from algorithms.maths.pythagoras import pythagoras
from algorithms.maths.rabin_miller import is_prime
from algorithms.maths.recursive_binomial_coefficient import (
    recursive_binomial_coefficient,
)
from algorithms.maths.rsa import decrypt, encrypt, generate_key
from algorithms.maths.sqrt_precision_factor import square_root
from algorithms.maths.summing_digits import sum_dig_pow
from algorithms.maths.surface_area_of_torus import surface_area_of_torus

# Module-level imports for backward compatibility (tests use module.function syntax)
from algorithms.maths import chinese_remainder_theorem  # noqa: E402
from algorithms.maths import fft  # noqa: E402
from algorithms.maths import hailstone  # noqa: E402
from algorithms.maths import modular_inverse  # type: ignore[no-redef]  # noqa: E402

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

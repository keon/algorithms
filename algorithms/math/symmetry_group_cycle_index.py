"""
Symmetry Group Cycle Index

Compute the cycle index polynomial of the symmetric group S_n and use it
to count distinct configurations of grids under row/column permutations
via Burnside's lemma.

Reference: https://en.wikipedia.org/wiki/Cycle_index#Symmetric_group_Sn

Complexity:
    Time:  O(n!) for cycle index computation
    Space: O(n!) for memoization
"""

from __future__ import annotations

from fractions import Fraction

from algorithms.math.gcd import lcm
from algorithms.math.polynomial import Monomial, Polynomial


def cycle_product(m1: Monomial, m2: Monomial) -> Monomial:
    """Compute the cycle product of two monomials from cycle indices.

    Args:
        m1: First monomial from a cycle index.
        m2: Second monomial from a cycle index.

    Returns:
        The resultant monomial from the Cartesian product merging.
    """
    assert isinstance(m1, Monomial) and isinstance(m2, Monomial)
    a_vars = m1.variables
    b_vars = m2.variables
    result_variables: dict[int, int] = dict()
    for i in a_vars:
        for j in b_vars:
            k = lcm(i, j)
            g = (i * j) // k
            if k in result_variables:
                result_variables[k] += a_vars[i] * b_vars[j] * g
            else:
                result_variables[k] = a_vars[i] * b_vars[j] * g

    return Monomial(result_variables, Fraction(m1.coeff * m2.coeff, 1))


def cycle_product_for_two_polynomials(
    p1: Polynomial, p2: Polynomial, q: float | int | Fraction
) -> float | int | Fraction:
    """Compute the product of two cycle indices and evaluate at q.

    Args:
        p1: First cycle index polynomial.
        p2: Second cycle index polynomial.
        q: The value to substitute for all variables.

    Returns:
        The evaluated result.
    """
    ans = Fraction(0, 1)
    for m1 in p1.monomials:
        for m2 in p2.monomials:
            ans += cycle_product(m1, m2).substitute(q)

    return ans


def _cycle_index_sym_helper(n: int, memo: dict[int, Polynomial]) -> Polynomial:
    """Recursively compute the cycle index of S_n with memoization.

    Args:
        n: The order of the symmetric group.
        memo: Dictionary of precomputed cycle indices.

    Returns:
        The cycle index polynomial of S_n.
    """
    if n in memo:
        return memo[n]
    ans = Polynomial([Monomial({}, Fraction(0, 1))])
    for t in range(1, n + 1):
        ans = ans.__add__(
            Polynomial([Monomial({t: 1}, Fraction(1, 1))])
            * _cycle_index_sym_helper(n - t, memo)
        )
    ans *= Fraction(1, n)
    memo[n] = ans
    return memo[n]


def get_cycle_index_sym(n: int) -> Polynomial:
    """Compute the cycle index of the symmetric group S_n.

    Args:
        n: The order of the symmetric group (non-negative integer).

    Returns:
        The cycle index as a Polynomial.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> get_cycle_index_sym(1)  # doctest: +SKIP
        Polynomial(...)
    """
    if n < 0:
        raise ValueError("n should be a non-negative integer.")

    memo = {
        0: Polynomial([Monomial({}, Fraction(1, 1))]),
        1: Polynomial([Monomial({1: 1}, Fraction(1, 1))]),
        2: Polynomial(
            [Monomial({1: 2}, Fraction(1, 2)), Monomial({2: 1}, Fraction(1, 2))]
        ),
        3: Polynomial(
            [
                Monomial({1: 3}, Fraction(1, 6)),
                Monomial({1: 1, 2: 1}, Fraction(1, 2)),
                Monomial({3: 1}, Fraction(1, 3)),
            ]
        ),
        4: Polynomial(
            [
                Monomial({1: 4}, Fraction(1, 24)),
                Monomial({2: 1, 1: 2}, Fraction(1, 4)),
                Monomial({3: 1, 1: 1}, Fraction(1, 3)),
                Monomial({2: 2}, Fraction(1, 8)),
                Monomial({4: 1}, Fraction(1, 4)),
            ]
        ),
    }
    result = _cycle_index_sym_helper(n, memo)
    return result

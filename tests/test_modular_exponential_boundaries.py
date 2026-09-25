"""Regression coverage for the modular identity at exponent zero."""

import pytest

from algorithms.math.modular_exponential import modular_exponential


@pytest.mark.parametrize("base", [-20, -1, 0, 1, 20])
@pytest.mark.parametrize("exponent", [0, 1, 2, 7])
@pytest.mark.parametrize("modulus", [-11, -2, -1, 1, 2, 11])
def test_matches_builtin_pow(base, exponent, modulus):
    assert modular_exponential(base, exponent, modulus) == pow(base, exponent, modulus)


def test_zero_modulus_still_raises():
    with pytest.raises(ZeroDivisionError):
        modular_exponential(7, 0, 0)

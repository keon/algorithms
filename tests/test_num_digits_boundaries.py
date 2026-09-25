"""Integer boundary oracles, including values beyond string conversion limits."""

import pytest

from algorithms.math.num_digits import num_digits


@pytest.mark.parametrize("exponent", [1, 2, 15, 16, 20, 100, 1000, 5000])
@pytest.mark.parametrize("sign", [-1, 1])
def test_neighbors_of_powers_of_ten(exponent, sign):
    power = 10**exponent
    assert num_digits(sign * (power - 1)) == exponent
    assert num_digits(sign * power) == exponent + 1
    assert num_digits(sign * (power + 1)) == exponent + 1


def test_small_integer_oracle():
    for value in range(-2000, 2001):
        assert num_digits(value) == len(str(abs(value)))

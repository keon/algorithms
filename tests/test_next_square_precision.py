"""Perfect-square decisions must not depend on floating-point rounding."""

import pytest

from algorithms.math.next_perfect_square import find_next_square, find_next_square2


@pytest.mark.parametrize("function", [find_next_square, find_next_square2])
@pytest.mark.parametrize("root", [2**27 + 1, 10**16, 2**100 + 1, 10**200])
def test_large_square_and_adjacent_integers(function, root):
    """Construct known squares and their nonsquare neighbors exactly."""
    square = root * root
    assert function(square) == (root + 1) * (root + 1)
    assert function(square - 1) == -1
    assert function(square + 1) == -1


@pytest.mark.parametrize("function", [find_next_square, find_next_square2])
@pytest.mark.parametrize(
    "value,expected",
    [(0, 1), (1, 4), (121, 144), (10, -1), (121.0, 144), (1.25, -1), (0.25, -1)],
)
def test_small_integer_and_float_inputs(function, value, expected):
    """Retain support for ordinary nonnegative integer and float inputs."""
    assert function(value) == expected
    assert isinstance(function(value), int)


@pytest.mark.parametrize("function", [find_next_square, find_next_square2])
def test_nearby_float_is_not_a_square(function):
    """An integer-valued float can still be a nonsquare despite a rounded root."""
    assert function(float(2**54 + 4)) == -1


@pytest.mark.parametrize("function", [find_next_square, find_next_square2])
def test_small_domain_matches_constructed_squares(function):
    """Enumerate expected results without computing approximate square roots."""
    expected = {root * root: (root + 1) ** 2 for root in range(101)}
    for value in range(10_001):
        assert function(value) == expected.get(value, -1)

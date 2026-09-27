"""Inversion supports float matrices while preserving exact integer results."""

from copy import deepcopy
from fractions import Fraction

import pytest

from algorithms.matrix.matrix_inversion import invert_matrix


@pytest.mark.parametrize(
    "matrix",
    [
        [[1.0, 1.0], [1.0, 2.0]],
        [[1.0, 0, 0], [0, 2.0, 0], [0, 0, 4.0]],
        [[1.5, 1.0, 0.5], [0.0, 2.0, 1.0], [1.0, 0.0, 3.0]],
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        [[4.0, 1, 0, 0], [2, 3.0, 1, 0], [0, 1, 2.0, 1], [0, 0, 1, 2.0]],
    ],
)
def test_float_inverse_is_two_sided(matrix):
    """Multiplication on either side recovers identity without input mutation."""
    original = deepcopy(matrix)
    inverse = invert_matrix(matrix)
    size = len(matrix)
    assert len(inverse) == size
    assert all(len(row) == size for row in inverse)
    for left, right in [(matrix, inverse), (inverse, matrix)]:
        for row in range(size):
            for column in range(size):
                value = sum(left[row][k] * right[k][column] for k in range(size))
                assert value == pytest.approx(int(row == column), abs=1e-12)
    assert matrix == original


def test_integer_inverse_keeps_exact_fractions():
    """Do not trade exact rational arithmetic for float support."""
    matrix = [[2, 0, 0], [0, 3, 0], [0, 0, 7]]
    inverse = invert_matrix(matrix)
    assert all(isinstance(value, Fraction) for row in inverse for value in row)
    assert inverse == [
        [Fraction(1, 2), 0, 0],
        [0, Fraction(1, 3), 0],
        [0, 0, Fraction(1, 7)],
    ]


def test_singular_float_matrix_keeps_error_sentinel():
    """The existing singularity check runs before dividing by determinant."""
    assert invert_matrix([[1.0, 2, 3], [1.0, 2, 3], [4.0, 5, 6]]) == [[-4]]

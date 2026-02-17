"""
Matrix Inversion

Compute the inverse of an invertible n x n matrix A, returning an n x n
matrix B such that A * B = B * A = I (the identity matrix). Uses cofactor
expansion: compute the matrix of minors with checkerboard signs, adjugate
(transpose), and multiply by 1/determinant.

Reference: https://en.wikipedia.org/wiki/Invertible_matrix

Complexity:
    Time:  O(n! * n)  (cofactor expansion)
    Space: O(n^2)
"""

from __future__ import annotations

import fractions


def invert_matrix(
    matrix: list[list[int | float]],
) -> list[list[int | float | fractions.Fraction]]:
    """Invert an n x n matrix.

    Args:
        matrix: Square matrix of size n x n (n >= 2).

    Returns:
        Inverted matrix, or an error sentinel:
        [[-1]] if not a valid matrix, [[-2]] if not square,
        [[-3]] if too small, [[-4]] if singular.

    Examples:
        >>> invert_matrix([[1, 1], [1, 2]])
        [[2, -1], [-1, 1]]
    """
    if not _array_is_matrix(matrix):
        return [[-1]]
    elif len(matrix) != len(matrix[0]):
        return [[-2]]
    elif len(matrix) < 2:
        return [[-3]]
    elif get_determinant(matrix) == 0:
        return [[-4]]
    elif len(matrix) == 2:
        multiplier = 1 / get_determinant(matrix)
        inverted = [[multiplier] * len(matrix) for _ in range(len(matrix))]
        inverted[0][1] = inverted[0][1] * -1 * matrix[0][1]
        inverted[1][0] = inverted[1][0] * -1 * matrix[1][0]
        inverted[0][0] = multiplier * matrix[1][1]
        inverted[1][1] = multiplier * matrix[0][0]
        return inverted
    else:
        matrix_of_minors = _get_matrix_of_minors(matrix)
        multiplier = fractions.Fraction(1, get_determinant(matrix))
        inverted = _transpose_and_multiply(matrix_of_minors, multiplier)
        return inverted


def get_determinant(matrix: list[list[int | float]]) -> int | float:
    """Recursively compute the determinant of an n x n matrix.

    Args:
        matrix: Square matrix of size n x n (n >= 2).

    Returns:
        Determinant value.

    Examples:
        >>> get_determinant([[1, 2], [3, 4]])
        -2
    """
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    sign = 1
    det = 0
    for i in range(len(matrix)):
        det += sign * matrix[0][i] * get_determinant(_get_minor(matrix, 0, i))
        sign *= -1
    return det


def _get_matrix_of_minors(
    matrix: list[list[int | float]],
) -> list[list[int | float]]:
    """Compute the matrix of minors with alternating signs (cofactor matrix).

    Args:
        matrix: Square matrix of size n x n.

    Returns:
        Cofactor matrix.
    """
    size = len(matrix)
    result = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(len(matrix[0])):
            sign = 1 if (row + col) % 2 == 0 else -1
            result[row][col] = sign * get_determinant(
                _get_minor(matrix, row, col)
            )
    return result


def _get_minor(
    matrix: list[list[int | float]], row: int, col: int
) -> list[list[int | float]]:
    """Extract the minor by removing the given row and column.

    Args:
        matrix: Square matrix.
        row: Row index to remove.
        col: Column index to remove.

    Returns:
        Sub-matrix with the specified row and column removed.
    """
    minors = []
    for i in range(len(matrix)):
        if i != row:
            new_row = matrix[i][:col]
            new_row.extend(matrix[i][col + 1:])
            minors.append(new_row)
    return minors


def _transpose_and_multiply(
    matrix: list[list[int | float]],
    multiplier: int | float | fractions.Fraction = 1,
) -> list[list[int | float | fractions.Fraction]]:
    """Transpose the matrix and multiply each element by a scalar.

    Args:
        matrix: Square matrix to transpose.
        multiplier: Scalar to multiply each element by.

    Returns:
        Transposed and scaled matrix.
    """
    for row in range(len(matrix)):
        for col in range(row + 1):
            temp = matrix[row][col] * multiplier
            matrix[row][col] = matrix[col][row] * multiplier
            matrix[col][row] = temp
    return matrix


def _array_is_matrix(matrix: list[list]) -> bool:
    """Check whether a 2D list has consistent row lengths.

    Args:
        matrix: 2D list to validate.

    Returns:
        True if all rows have the same length, False otherwise.
    """
    if len(matrix) == 0:
        return False
    first_col = len(matrix[0])
    for row in matrix:
        if len(row) != first_col:
            return False
    return True

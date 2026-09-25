"""Large-offset regressions must not be mistaken for vertical lines."""

import statistics

import pytest

from algorithms.math.linear_regression import linear_regression, r_squared, rmse


@pytest.mark.parametrize("x_offset", [0, 10**8, 10**12, -(10**12)])
@pytest.mark.parametrize("y_offset", [0, 10**12, -(10**12)])
def test_exact_line_after_translation(x_offset, y_offset):
    x = [float(x_offset + i) for i in range(5)]
    y = [float(y_offset + 2 * i) for i in range(5)]
    slope, intercept = linear_regression(x, y)
    assert slope == pytest.approx(2)
    assert intercept == pytest.approx(y_offset - 2 * x_offset)
    assert r_squared(x, y) == pytest.approx(1)
    assert rmse(x, y) == pytest.approx(0)


def test_noisy_offset_matches_standard_library():
    x = [10**12 + i for i in range(7)]
    y = [1, 4, 4, 8, 7, 12, 13]
    assert linear_regression(x, y) == pytest.approx(statistics.linear_regression(x, y))


def test_constant_x_still_raises():
    with pytest.raises(ValueError, match="undefined"):
        linear_regression([10**12, 10**12], [1, 2])


@pytest.mark.parametrize("offset", [1e16, -1e16])
def test_two_point_midpoint_is_not_rounded(offset):
    slope, intercept = linear_regression([offset, offset + 2], [0, 4])
    assert slope == 2
    assert intercept == -2 * offset


def test_large_offsets_on_both_axes():
    slope, intercept = linear_regression([1e16, 1e16 + 2], [1e16, 1e16 + 4])
    assert slope == 2
    assert intercept == -1e16

"""Cosine similarity is invariant under independent positive scaling."""

import math
import sys

import pytest

from algorithms.math.cosine_similarity import cosine_similarity


@pytest.mark.parametrize("left_scale", [1e-200, 1.0, 1e200])
@pytest.mark.parametrize("right_scale", [1e-200, 1.0, 1e200])
def test_independent_vector_scales(left_scale, right_scale):
    """Same, opposite, perpendicular and general directions retain their angle."""
    cases = [
        ([1, 2, 3], [1, 2, 3], 1.0),
        ([1, 2, 3], [-1, -2, -3], -1.0),
        ([1, 2, 3], [2, -1, 0], 0.0),
        ([1, 2, 3], [1, -1, 2], 5 / math.sqrt(84)),
    ]
    for left, right, expected in cases:
        scaled_left = [value * left_scale for value in left]
        scaled_right = [value * right_scale for value in right]
        result = cosine_similarity(scaled_left, scaled_right)
        assert math.isfinite(result)
        assert result == pytest.approx(expected, abs=1e-15)


@pytest.mark.parametrize("magnitude", [sys.float_info.max, math.ulp(0.0)])
def test_extreme_representable_components(magnitude):
    """Even a nonrepresentable raw norm must not spoil a representable cosine."""
    same = cosine_similarity([magnitude, magnitude], [magnitude, magnitude])
    orthogonal = cosine_similarity([magnitude, magnitude], [magnitude, -magnitude])
    assert same == pytest.approx(1)
    assert orthogonal == pytest.approx(0)


@pytest.mark.parametrize("left,right", [([], []), ([0, 0], [1, 2]), ([1, 2], [0, 0])])
def test_zero_vector_exception_is_preserved(left, right):
    """Zero vectors still have undefined similarity and raise the existing error."""
    with pytest.raises(ZeroDivisionError):
        cosine_similarity(left, right)


def test_dimension_validation_is_preserved():
    """Mismatched vector lengths keep their explicit validation error."""
    with pytest.raises(ValueError, match="same length"):
        cosine_similarity([1], [1, 2])

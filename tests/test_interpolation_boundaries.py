"""Interpolation search must handle equal endpoint values safely."""

from itertools import combinations_with_replacement

import pytest

from algorithms.searching.interpolation_search import interpolation_search


@pytest.mark.parametrize(
    "values,target",
    [
        ([5], 5),
        ([0], 0),
        ([-2], -2),
        ([7, 7, 7], 7),
        ([0, 1, 100], 1),
        ([0, 10**100, 10**200], 10**100),
        ([10**400], 10**400),
    ],
)
def test_matches_at_equal_bounds(values, target):
    """Singleton intervals remain searchable, including after narrowing."""
    index = interpolation_search(values, target)
    assert 0 <= index < len(values)
    assert values[index] == target


@pytest.mark.parametrize(
    "values,target",
    [([], 1), ([5], 4), ([5], 6), ([7, 7, 7], 6), ([7, 7, 7], 8)],
)
def test_absent_values(values, target):
    """An empty interval or an out-of-bounds target has no match."""
    assert interpolation_search(values, target) == -1


def test_small_sorted_arrays_match_membership():
    """Enumerate duplicate-containing sorted arrays against list membership."""
    for length in range(7):
        for values in combinations_with_replacement(range(-2, 3), length):
            for target in range(-3, 4):
                index = interpolation_search(list(values), target)
                if target in values:
                    assert 0 <= index < len(values), (values, target)
                    assert values[index] == target, (values, target)
                else:
                    assert index == -1, (values, target)

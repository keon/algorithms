"""
Set Cover Problem

Given a universe U of n elements, a collection S of subsets of U, and a cost
for each subset, find the minimum-cost sub-collection that covers all of U.

Reference: https://en.wikipedia.org/wiki/Set_cover_problem

Complexity:
    optimal_set_cover:
        Time:  O(2^m * n) where m is the number of subsets
        Space: O(2^m)
    greedy_set_cover:
        Time:  O(m * n)
        Space: O(n)
"""

from __future__ import annotations

from itertools import chain, combinations


def _powerset(iterable: list[str]) -> chain[tuple[str, ...]]:
    """Generate all subsets of the iterable.

    Args:
        iterable: Input collection.

    Returns:
        An iterator over all subsets (the power set).
    """
    items = list(iterable)
    return chain.from_iterable(
        combinations(items, r) for r in range(len(items) + 1)
    )


def optimal_set_cover(
    universe: set[int],
    subsets: dict[str, set[int]],
    costs: dict[str, int],
) -> tuple[str, ...] | None:
    """Find the minimum-cost exact set cover via brute force.

    Warning: O(2^m) complexity -- do not use on large inputs.

    Args:
        universe: The set of all elements to cover.
        subsets: Mapping of subset name to its elements.
        costs: Mapping of subset name to its cost.

    Returns:
        A tuple of subset names forming the optimal cover, or None if
        no cover exists.

    Examples:
        >>> universe = {1, 2, 3, 4, 5}
        >>> subsets = {'S1': {4, 1, 3}, 'S2': {2, 5}, 'S3': {1, 4, 3, 2}}
        >>> costs = {'S1': 5, 'S2': 10, 'S3': 3}
        >>> optimal_set_cover(universe, subsets, costs)
        ('S2', 'S3')
    """
    pset = _powerset(list(subsets.keys()))
    best_set: tuple[str, ...] | None = None
    best_cost = float("inf")
    for subset in pset:
        covered: set[int] = set()
        cost = 0
        for name in subset:
            covered.update(subsets[name])
            cost += costs[name]
        if len(covered) == len(universe) and cost < best_cost:
            best_set = subset
            best_cost = cost
    return best_set


def greedy_set_cover(
    universe: set[int],
    subsets: dict[str, set[int]],
    costs: dict[str, int],
) -> list[str] | None:
    """Find an approximate set cover using a greedy approach.

    Args:
        universe: The set of all elements to cover.
        subsets: Mapping of subset name to its elements.
        costs: Mapping of subset name to its cost.

    Returns:
        A list of subset names forming the greedy cover, or None if the
        subsets do not cover the universe.

    Examples:
        >>> universe = {1, 2, 3, 4, 5}
        >>> subsets = {'S1': {4, 1, 3}, 'S2': {2, 5}, 'S3': {1, 4, 3, 2}}
        >>> costs = {'S1': 5, 'S2': 10, 'S3': 3}
        >>> greedy_set_cover(universe, subsets, costs)
        ['S3', 'S2']
    """
    all_elements = set(e for s in subsets.values() for e in s)
    if all_elements != universe:
        return None

    covered: set[int] = set()
    cover_sets: list[str] = []

    while covered != universe:
        min_cost_elem_ratio = float("inf")
        min_set: str | None = None
        for name, elements in subsets.items():
            new_elements = len(elements - covered)
            if new_elements != 0:
                cost_elem_ratio = costs[name] / new_elements
                if cost_elem_ratio < min_cost_elem_ratio:
                    min_cost_elem_ratio = cost_elem_ratio
                    min_set = name
        cover_sets.append(min_set)
        covered |= subsets[min_set]
    return cover_sets

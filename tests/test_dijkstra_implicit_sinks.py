"""Neighbor-only vertices have an empty adjacency list, not a missing path."""

from copy import deepcopy

import pytest

from algorithms.graph.dijkstra_heapq import dijkstra


@pytest.mark.parametrize(
    "graph,source,target,expected",
    [
        ({"s": {"a": 1, "t": 2}}, "s", "t", (2, ["s", "t"])),
        ({"s": {"a": 1}}, "s", "missing", (float("inf"), [])),
        ({"s": {"a": 1}}, "s", "a", (1, ["s", "a"])),
        ({"s": {"a": 0, "b": 1}, "b": {"t": 2}}, "s", "t", (3, ["s", "b", "t"])),
        ({"s": {"a": 1}}, "s", "s", (0, ["s"])),
    ],
)
def test_missing_sink_adjacency(graph, source, target, expected):
    """A dead end must not prevent another target from being reached."""
    original = deepcopy(graph)
    assert dijkstra(graph, source, target) == expected
    assert graph == original


def test_implicit_and_explicit_sinks_give_the_same_result():
    """Omitting terminal empty dictionaries does not change shortest paths."""
    graph = {"s": {"a": 1, "b": 4, "dead": 0}, "a": {"b": 1, "t": 6}, "b": {"t": 2}}
    complete = {**graph, "dead": {}, "t": {}}
    for target in ["s", "a", "b", "dead", "t", "missing", ""]:
        assert dijkstra(graph, "s", target) == dijkstra(complete, "s", target)

"""Tests for algorithms added to resolve open GitHub issues."""

from __future__ import annotations

import unittest

from algorithms.common.tree_node import TreeNode
from algorithms.data_structures import SqrtDecomposition
from algorithms.graph.dijkstra_heapq import dijkstra
from algorithms.math.goldbach import goldbach, verify_goldbach
from algorithms.tree.binary_tree_views import (
    bottom_view,
    left_view,
    right_view,
    top_view,
)

# ── Dijkstra with priority queue (#565) ────────────────────────────────


class TestDijkstraHeapq(unittest.TestCase):
    """Tests for the heap-based Dijkstra implementation."""

    def setUp(self):
        self.graph = {
            "s": {"a": 2, "b": 1},
            "a": {"s": 3, "b": 4, "c": 8},
            "b": {"s": 4, "a": 2, "d": 2},
            "c": {"a": 2, "d": 7, "t": 4},
            "d": {"b": 1, "c": 11, "t": 5},
            "t": {"c": 3, "d": 5},
        }

    def test_shortest_path(self):
        dist, path = dijkstra(self.graph, "s", "t")
        self.assertEqual(dist, 8)
        self.assertEqual(path, ["s", "b", "d", "t"])

    def test_same_source_and_target(self):
        dist, path = dijkstra(self.graph, "s", "s")
        self.assertEqual(dist, 0)
        self.assertEqual(path, ["s"])

    def test_direct_neighbor(self):
        dist, path = dijkstra(self.graph, "s", "b")
        self.assertEqual(dist, 1)
        self.assertEqual(path, ["s", "b"])

    def test_unreachable_target(self):
        graph = {"a": {"b": 1}, "b": {}, "c": {}}
        dist, path = dijkstra(graph, "a", "c")
        self.assertEqual(dist, float("inf"))
        self.assertEqual(path, [])

    def test_single_node(self):
        graph = {"a": {}}
        dist, path = dijkstra(graph, "a", "a")
        self.assertEqual(dist, 0)
        self.assertEqual(path, ["a"])

    def test_triangle(self):
        graph = {"a": {"b": 1, "c": 4}, "b": {"c": 2}, "c": {}}
        dist, path = dijkstra(graph, "a", "c")
        self.assertEqual(dist, 3)
        self.assertEqual(path, ["a", "b", "c"])


# ── Goldbach's conjecture (#908) ────────────────────────────────────────


class TestGoldbach(unittest.TestCase):
    """Tests for Goldbach's conjecture decomposition."""

    def test_small_even(self):
        self.assertEqual(goldbach(4), (2, 2))

    def test_goldbach_28(self):
        p, q = goldbach(28)
        self.assertEqual(p + q, 28)
        self.assertTrue(p <= q)

    def test_goldbach_100(self):
        p, q = goldbach(100)
        self.assertEqual(p + q, 100)

    def test_goldbach_large(self):
        p, q = goldbach(1000)
        self.assertEqual(p + q, 1000)

    def test_odd_raises(self):
        with self.assertRaises(ValueError):
            goldbach(7)

    def test_two_raises(self):
        with self.assertRaises(ValueError):
            goldbach(2)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            goldbach(-4)

    def test_verify_range(self):
        self.assertTrue(verify_goldbach(200))


# ── Binary tree views (#829) ────────────────────────────────────────────


class TestBinaryTreeViews(unittest.TestCase):
    """Tests for left/right/top/bottom tree views."""

    def setUp(self):
        """Build a tree:
                1
               / \\
              2   3
             / \\   \\
            4   5   6
        """
        self.root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, None, TreeNode(6)),
        )

    def test_left_view(self):
        self.assertEqual(left_view(self.root), [1, 2, 4])

    def test_right_view(self):
        self.assertEqual(right_view(self.root), [1, 3, 6])

    def test_top_view(self):
        self.assertEqual(top_view(self.root), [4, 2, 1, 3, 6])

    def test_bottom_view(self):
        self.assertEqual(bottom_view(self.root), [4, 2, 5, 3, 6])

    def test_empty_tree(self):
        self.assertEqual(left_view(None), [])
        self.assertEqual(right_view(None), [])
        self.assertEqual(top_view(None), [])
        self.assertEqual(bottom_view(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(left_view(root), [42])
        self.assertEqual(right_view(root), [42])
        self.assertEqual(top_view(root), [42])
        self.assertEqual(bottom_view(root), [42])

    def test_left_skewed(self):
        """
            1
           /
          2
         /
        3
        """
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(left_view(root), [1, 2, 3])
        self.assertEqual(right_view(root), [1, 2, 3])

    def test_right_skewed(self):
        """
        1
         \\
          2
           \\
            3
        """
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(left_view(root), [1, 2, 3])
        self.assertEqual(right_view(root), [1, 2, 3])


# ── Square root decomposition (#651) ────────────────────────────────────


class TestSqrtDecomposition(unittest.TestCase):
    """Tests for square root decomposition range queries."""

    def test_full_range_sum(self):
        sd = SqrtDecomposition([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sd.query(0, 8), 45)

    def test_partial_range(self):
        sd = SqrtDecomposition([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sd.query(2, 5), 18)  # 3+4+5+6

    def test_single_element(self):
        sd = SqrtDecomposition([10, 20, 30])
        self.assertEqual(sd.query(1, 1), 20)

    def test_update(self):
        sd = SqrtDecomposition([1, 2, 3, 4, 5])
        sd.update(2, 10)
        self.assertEqual(sd.query(0, 4), 22)  # 1+2+10+4+5

    def test_update_full_range(self):
        sd = SqrtDecomposition([1, 2, 3, 4, 5, 6, 7, 8, 9])
        sd.update(4, 10)
        self.assertEqual(sd.query(0, 8), 50)

    def test_multiple_updates(self):
        sd = SqrtDecomposition([1, 1, 1, 1, 1])
        sd.update(0, 5)
        sd.update(4, 5)
        self.assertEqual(sd.query(0, 4), 13)  # 5+1+1+1+5

    def test_out_of_range_update(self):
        sd = SqrtDecomposition([1, 2, 3])
        with self.assertRaises(IndexError):
            sd.update(5, 10)

    def test_invalid_query(self):
        sd = SqrtDecomposition([1, 2, 3])
        with self.assertRaises(IndexError):
            sd.query(0, 5)

    def test_small_array(self):
        sd = SqrtDecomposition([42])
        self.assertEqual(sd.query(0, 0), 42)
        sd.update(0, 100)
        self.assertEqual(sd.query(0, 0), 100)

    def test_larger_array(self):
        arr = list(range(1, 101))  # 1..100
        sd = SqrtDecomposition(arr)
        self.assertEqual(sd.query(0, 99), 5050)
        self.assertEqual(sd.query(0, 9), 55)  # 1+2+...+10


if __name__ == "__main__":
    unittest.main()

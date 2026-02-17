
from topological import topological_sort

import unittest

class TestTopologicalSort(unittest.TestCase):
    def test_simple_dag(self):
        vertices = 6
        edges = [
            (5, 2),
            (5, 0),
            (4, 0),
            (4, 1),
            (2, 3),
            (3, 1)
        ]

        order = topological_sort(vertices, edges)

        # Verify correct length
        self.assertEqual(len(order), vertices)

        # Verify constraints
        position = {node: i for i, node in enumerate(order)}
        for u, v in edges:
            self.assertLess(position[u], position[v])

    def test_single_vertex(self):
        vertices = 1
        edges = []

        order = topological_sort(vertices, edges)
        self.assertEqual(order, [0])

    def test_disconnected_graph(self):
        vertices = 4
        edges = [
            (0, 1),
            (2, 3)
        ]

        order = topological_sort(vertices, edges)

        self.assertEqual(len(order), vertices)

        position = {node: i for i, node in enumerate(order)}
        for u, v in edges:
            self.assertLess(position[u], position[v])

    def test_no_edges(self):
        vertices = 5
        edges = []

        order = topological_sort(vertices, edges)

        self.assertEqual(len(order), vertices)
        self.assertCountEqual(order, [0, 1, 2, 3, 4])

    def test_cycle_detection(self):
        vertices = 3
        edges = [
            (0, 1),
            (1, 2),
            (2, 0)
        ]

        with self.assertRaises(ValueError):
            topological_sort(vertices, edges)

    def test_self_loop_cycle(self):
        vertices = 2
        edges = [
            (0, 0)
        ]

        with self.assertRaises(ValueError):
            topological_sort(vertices, edges)


if __name__ == "__main__":
    unittest.main()
from algorithms.graph import Tarjan
from algorithms.graph import check_bipartite

import unittest


class TestTarjan(unittest.TestCase):
    """
    Test for the file tarjan.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_tarjan_example_1(self):
        # Graph from https://en.wikipedia.org/wiki/File:Scc.png
        example = {
            'A': ['B'],
            'B': ['C', 'E', 'F'],
            'C': ['D', 'G'],
            'D': ['C', 'H'],
            'E': ['A', 'F'],
            'F': ['G'],
            'G': ['F'],
            'H': ['D', 'G']
        }

        g = Tarjan(example)
        self.assertEqual(g.sccs, [['F', 'G'], ['C', 'D', 'H'], ['A', 'B', 'E']])

    def test_tarjan_example_2(self):
        # Graph from https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm#/media/File:Tarjan%27s_Algorithm_Animation.gif
        example = {
            'A': ['E'],
            'B': ['A'],
            'C': ['B', 'D'],
            'D': ['C'],
            'E': ['B'],
            'F': ['B', 'E', 'G'],
            'G': ['F', 'C'],
            'H': ['G', 'H', 'D']
        }

        g = Tarjan(example)
        self.assertEqual(g.sccs, [['A', 'B', 'E'], ['C', 'D'], ['F', 'G'], ['H']])

        
class TestCheckBipartite(unittest.TestCase):
    
    def test_check_bipartite(self):
        
        adj_list_1 = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        self.assertEqual(True, check_bipartite(adj_list_1))
        
        adj_list_2 = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        self.assertEqual(True, check_bipartite(adj_list_2))
        
        adj_list_3 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
        self.assertEqual(False, check_bipartite(adj_list_3))

from algorithms.graph import Tarjan
from algorithms.graph import check_bipartite
from algorithms.graph.dijkstra import Dijkstra
from algorithms.graph import maximum_flow_bfs
from algorithms.graph import maximum_flow_dfs

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

class TestDijkstra(unittest.TestCase):
    
    def test_dijkstra(self):
        g = Dijkstra(9) 
        g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 

        self.assertEqual(g.dijkstra(0), [0, 4, 12, 19, 21, 11, 9, 8, 14])

class TestMaximum_Flow_Bfs(unittest.TestCase):

    """
    Test for the file def maximum_flow_bfs.py
    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_maximum_flow_bfs(self):
        graph = [[0, 16, 13, 0, 0, 0], [0, 0, 10, 12, 0, 0], [0, 4, 0, 0, 14, 0], [0, 0, 9, 0, 0, 20], [0, 0, 0, 7, 0, 4], [0, 0, 0, 0, 0, 0]]
        maximum_flow = maximum_flow_bfs(graph)

        self.assertEqual(maximum_flow, 23)

class TestMaximum_Flow_Dfs(unittest.TestCase):

    """
    Test for the file def maximum_flow_dfs.py
    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_maximum_flow_dfs(self):
        graph = [[0, 16, 13, 0, 0, 0], [0, 0, 10, 12, 0, 0], [0, 4, 0, 0, 14, 0], [0, 0, 9, 0, 0, 20], [0, 0, 0, 7, 0, 4], [0, 0, 0, 0, 0, 0]]
        maximum_flow = maximum_flow_dfs(graph)

        self.assertEqual(maximum_flow, 23)

if __name__ == '__main__':
    unittest.main()
    
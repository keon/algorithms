from algorithms.graph import Tarjan
from algorithms.graph import check_bipartite
from algorithms.graph.dijkstra import Dijkstra
from algorithms.graph import ford_fulkerson
from algorithms.graph import edmonds_karp
from algorithms.graph import dinic
from algorithms.graph import maximum_flow_bfs
from algorithms.graph import maximum_flow_dfs
from algorithms.graph import all_pairs_shortest_path
from algorithms.graph import bellman_ford
from algorithms.graph import count_connected_number_of_component
from algorithms.graph import prims_minimum_spanning
from algorithms.graph import astar_pathfinding

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
        self.assertEqual(g.sccs, [['F', 'G'], ['C', 'D', 'H'],
                                  ['A', 'B', 'E']])

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
        self.assertEqual(g.sccs, [['A', 'B', 'E'], ['C', 'D'], ['F', 'G'],
                                  ['H']])


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
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]]

        self.assertEqual(g.dijkstra(0), [0, 4, 12, 19, 21, 11, 9, 8, 14])


class TestMaximumFlow(unittest.TestCase):
    """
    Test for the file maximum_flow.py

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_ford_fulkerson(self):
        capacity = [
                [0, 10, 10, 0, 0, 0, 0],
                [0, 0, 2, 0, 4, 8, 0],
                [0, 0, 0, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 6, 0, 10],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(19, ford_fulkerson(capacity, 0, 6))

    def test_edmonds_karp(self):
        capacity = [
                [0, 10, 10, 0, 0, 0, 0],
                [0, 0, 2, 0, 4, 8, 0],
                [0, 0, 0, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 6, 0, 10],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(19, edmonds_karp(capacity, 0, 6))

    def dinic(self):
        capacity = [
                [0, 10, 10, 0, 0, 0, 0],
                [0, 0, 2, 0, 4, 8, 0],
                [0, 0, 0, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 6, 0, 10],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(19, dinic(capacity, 0, 6))


class TestMaximum_Flow_Bfs(unittest.TestCase):

    """
    Test for the file def maximum_flow_bfs.py
    Arguments:
        unittest {[type]} -- [description]
    """
    def test_maximum_flow_bfs(self):
        graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ]
        maximum_flow = maximum_flow_bfs(graph)

        self.assertEqual(maximum_flow, 23)


class TestMaximum_Flow_Dfs(unittest.TestCase):

    """
    Test for the file def maximum_flow_dfs.py
    Arguments:
        unittest {[type]} -- [description]
    """
    def test_maximum_flow_dfs(self):
        graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ]
        maximum_flow = maximum_flow_dfs(graph)

        self.assertEqual(maximum_flow, 23)


class TestAll_Pairs_Shortest_Path(unittest.TestCase):
    def test_all_pairs_shortest_path(self):
        graph = [[0, 0.1, 0.101, 0.142, 0.277],
                 [0.465, 0, 0.191, 0.192, 0.587],
                 [0.245, 0.554, 0, 0.333, 0.931],
                 [1.032, 0.668, 0.656, 0, 0.151],
                 [0.867, 0.119, 0.352, 0.398, 0]]
        result = all_pairs_shortest_path(graph)

        self.assertEqual(result, [
                                    [0, 0.1, 0.101, 0.142, 0.277],
                                    [0.436, 0, 0.191, 0.192,
                                     0.34299999999999997],
                                    [0.245, 0.345, 0, 0.333, 0.484],
                                    [0.706, 0.27, 0.46099999999999997, 0,
                                     0.151],
                                    [0.5549999999999999, 0.119, 0.31, 0.311,
                                     0],
                                ])


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        graph1 = {
            'a': {'b': 6, 'e': 7},
            'b': {'c': 5, 'd': -4, 'e': 8},
            'c': {'b': -2},
            'd': {'a': 2, 'c': 7},
            'e': {'b': -3}
        }
        self.assertEqual(True, bellman_ford(graph1, 'a'))
        graph2 = {
            'a': {'d': 3, 'e': 4},
            'b': {'a': 7, 'e': 2},
            'c': {'a': 12, 'd': 9, 'e': 11},
            'd': {'c': 5, 'e': 11},
            'e': {'a': 7, 'b': 5, 'd': 1}
        }
        self.assertEqual(True, bellman_ford(graph2, 'a'))


class TestConnectedComponentInGraph(unittest.TestCase):
    """
     Class for testing different cases for connected components in graph
    """
    def test_count_connected_components(self):
        """
           Test Function that test the different cases of count connected
           components
            2----------0    1--------5      3
            |
            |
            4
                output = 3
        """
        expected_result = 3
        # adjacency list representation of graph
        l = [[2],
             [5],
             [0,4],
             [],
             [2],
             [1]]

        size = 5
        result = count_connected_number_of_component.count_components(l, size)
        self.assertEqual(result, expected_result)

    def test_connected_components_with_empty_graph(self):

        """
            input :
            output : 0
        """
        l = [[]]
        expected_result = 0
        size = 0
        result = count_connected_number_of_component.count_components(l, size)
        self.assertEqual(result, expected_result)

    def test_connected_components_without_edges_graph(self):
        """
          input : 0          2             3          4
          output : 4
        """
        l = [[0], [], [2], [3], [4]]
        size = 4
        expected_result = 4
        result = count_connected_number_of_component.count_components(l, size)
        self.assertEqual(result, expected_result)


class PrimsMinimumSpanning(unittest.TestCase):
    def test_prim_spanning(self):
        graph1 = {
            1: [[3, 2], [8, 3]],
            2: [[3, 1], [5, 4]],
            3: [[8, 1], [2, 4], [4, 5]],
            4: [[5, 2], [2, 3], [6, 5]],
            5: [[4, 3], [6, 4]]
        }
        self.assertEqual(14, prims_minimum_spanning(graph1))
        graph2 = {
            1: [[7, 2], [6, 4]],
            2: [[7, 1], [9, 4], [6, 3]],
            3: [[8, 4], [6, 2]],
            4: [[6, 1], [9, 2], [8, 3]]
        }
        self.assertEqual(19, prims_minimum_spanning(graph2))

class TestAstarPathfinding(unittest.TestCase):
    class GridGraph:
        """
        A graph representing a 2D grid.
        """

        def __init__(self, grid: str):
            self.grid = list(grid.split())
            self.height = len(self.grid)
            self.width = len(self.grid[0]) if self.height != 0 else 0

        def adjacent(self, node):
            """ Get all nodes adjacent to the given node """
            x, y = node

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x+dx
                ny = y+dy

                if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                    # stay on grid
                    continue

                if self.grid[ny][nx] == '#':
                    # avoid walls
                    continue

                distance = (dx**2 + dy**2) ** 0.5
                yield ((x + dx, y + dy), distance)

        def distance_heuristic(self, source, target):
            """ estimate distance using euclidean distance """
            sx, sy = source
            tx, ty = target
            
            dx = sx - tx
            dy = sy - ty

            return ((dx**2 + dy**2) ** 0.5)

        def find(self, cell):
            """ Get the position of a character in the grid """
            for y, row in enumerate(self.grid):
                x = row.find(str(cell))
                if x != -1:
                    return (x, y)
            return None

    def test_grid_graph(self):
        graph = self.GridGraph("""
            ....
            .##.
            ..#.
        """)
        self.assertEqual(graph.width, 4)
        self.assertEqual(graph.height, 3)
        self.assertEqual(graph.grid, [
            "....",
            ".##.",
            "..#.",
        ])

        self.assertEqual(list(graph.adjacent((0, 0))), [
            ((1, 0), 1),
            ((0, 1), 1),
        ])

        self.assertEqual(list(graph.adjacent((0, 1))), [
            ((0, 0), 1),
            ((0, 2), 1),
        ])

    def test_astar_pathfinding(self):
        graph = self.GridGraph("""
            #######
            #456..#
            #3###.#
            #2#...#
            #10...#
            #######
        """)

        path = astar_pathfinding.find_path(graph, graph.find('0'), graph.find('6'))
        self.assertEqual(path, [graph.find(x) for x in range(7)])

    def test_astar_pathfinding_2(self):
        graph = self.GridGraph("""
            #############
            #....#qpon..#
            #.#######m#.#
            #.#.abcd#lk.#
            #.#.###e##j##
            #......fghi.#
            #############
        """)

        path = astar_pathfinding.find_path(graph, graph.find('a'), graph.find('q'))
        self.assertEqual(path, [graph.find(chr(x)) for x in range(ord('a'), ord('q')+1)])



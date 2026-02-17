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
from algorithms.graph import check_digraph_strongly_connected
from algorithms.graph import cycle_detection
from algorithms.graph import find_path
from algorithms.graph import path_between_two_vertices_in_digraph
from algorithms.graph import strongly_connected_components_kosaraju

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

class TestDigraphStronglyConnected(unittest.TestCase):
    def test_digraph_strongly_connected(self):
        g1 = check_digraph_strongly_connected.Graph(5)
        g1.add_edge(0, 1)
        g1.add_edge(1, 2)
        g1.add_edge(2, 3)
        g1.add_edge(3, 0)
        g1.add_edge(2, 4)
        g1.add_edge(4, 2)
        self.assertTrue(g1.is_strongly_connected())

        g2 = check_digraph_strongly_connected.Graph(4)
        g2.add_edge(0, 1)
        g2.add_edge(1, 2)
        g2.add_edge(2, 3)
        self.assertFalse(g2.is_strongly_connected())

class TestCycleDetection(unittest.TestCase):
    def test_cycle_detection_with_cycle(self):
        graph = {'A': ['B', 'C'],
                 'B': ['D'],
                 'C': ['F'],
                 'D': ['E', 'F'],
                 'E': ['B'],
                 'F': []}
        self.assertTrue(cycle_detection.contains_cycle(graph))

    def test_cycle_detection_with_no_cycle(self):
        graph = {'A': ['B', 'C'],
                 'B': ['D', 'E'],
                 'C': ['F'],
                 'D': ['E'],
                 'E': [],
                 'F': []}
        self.assertFalse(cycle_detection.contains_cycle(graph))

class TestFindPath(unittest.TestCase):
    def test_find_all_paths(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D', 'F'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}

        paths = find_path.find_all_path(graph, 'A', 'F')
        print(paths)
        self.assertEqual(sorted(paths), sorted([
            ['A', 'C', 'F'],
            ['A', 'B', 'C', 'F'],
            ['A', 'B', 'D', 'C', 'F'],
        ]))

class TestPathBetweenTwoVertices(unittest.TestCase):
    def test_node_is_reachable(self):
        g = path_between_two_vertices_in_digraph.Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        self.assertTrue(g.is_reachable(1, 3))
        self.assertFalse(g.is_reachable(3, 1))

class TestStronglyConnectedComponentsKosaraju(unittest.TestCase):
    def test_kosaraju_algorithm(self):
        V = 6
        adj = [
            [2],
            [0],
            [3],
            [1, 4],
            [5],
            [4]
        ]

        result = strongly_connected_components_kosaraju.Kosaraju().kosaraju(V, adj)

        # Expected result: 2 strongly connected components
        self.assertEqual(result, 2)


# --- Tests merged from test_bfs.py ---

from algorithms.graph import (
    count_islands,
    maze_search,
    ladder_length,
)


class TestCountIslandsBfs(unittest.TestCase):

    def test_count_islands(self):
        grid_1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        self.assertEqual(1, count_islands(grid_1))
        grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 1]]
        self.assertEqual(3, count_islands(grid_2))
        grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
                  [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
        self.assertEqual(3, count_islands(grid_3))
        grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0]]
        self.assertEqual(5, count_islands(grid_4))


class TestMazeSearchBfs(unittest.TestCase):

    def test_maze_search(self):
        grid_1 = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1],
                  [1, 1, 1, 0, 1, 1]]
        self.assertEqual(14, maze_search(grid_1))
        grid_2 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(-1, maze_search(grid_2))


class TestWordLadder(unittest.TestCase):

    def test_ladder_length(self):

        # hit -> hot -> dot -> dog -> cog
        self.assertEqual(5, ladder_length('hit', 'cog', ["hot", "dot", "dog",
                                          "lot", "log"]))

        # pick -> sick -> sink -> sank -> tank == 5
        self.assertEqual(5, ladder_length('pick', 'tank',
                                          ['tock', 'tick', 'sank', 'sink',
                                           'sick']))

        # live -> life == 1, no matter what is the word_list.
        self.assertEqual(1, ladder_length('live', 'life', ['hoho', 'luck']))

        # 0 length from ate -> ate
        self.assertEqual(0, ladder_length('ate', 'ate', []))

        # not possible to reach !
        self.assertEqual(-1, ladder_length('rahul', 'coder', ['blahh',
                                           'blhah']))


# --- Tests merged from test_dfs.py ---

from algorithms.graph import (
    get_factors, get_factors_iterative1, get_factors_iterative2,
    num_islands_dfs,
    pacific_atlantic,
    Sudoku,
    walls_and_gates,
    find_path_dfs,
)


class TestAllFactors(unittest.TestCase):
    def test_get_factors(self):
        self.assertEqual([[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2],
                         [2, 4, 4], [4, 8]], get_factors(32))

    def test_get_factors_iterative1(self):
        self.assertEqual([[2, 16], [4, 8], [2, 2, 8], [2, 4, 4], [2, 2, 2, 4],
                          [2, 2, 2, 2, 2]], get_factors_iterative1(32))

    def test_get_factors_iterative2(self):
        self.assertEqual([[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 8], [2, 4, 4],
                          [2, 16], [4, 8]], get_factors_iterative2(32))


class TestCountIslandsDfs(unittest.TestCase):
    def test_num_islands(self):
        self.assertEqual(1, num_islands_dfs([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0],
                                         [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
        self.assertEqual(3, num_islands_dfs([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                                         [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]))


class TestPacificAtlantic(unittest.TestCase):
    def test_pacific_atlantic(self):
        self.assertEqual([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0],
                          [3, 1], [4, 0]], pacific_atlantic([[1, 2, 2, 3, 5],
                                                            [3, 2, 3, 4, 4],
                                                            [2, 4, 5, 3, 1],
                                                            [6, 7, 1, 4, 5],
                                                            [5, 1, 1, 2, 4]]))


class TestSudoku(unittest.TestCase):
    def test_sudoku_solver(self):
        board = [["5", "3", "."], ["6", ".", "."], [".", "9", "8"]]
        test_obj = Sudoku(board, 3, 3)
        test_obj.solve()
        self.assertEqual([['5', '3', '1'], ['6', '1', '2'],
                         ['1', '9', '8']], test_obj.board)


class TestWallsAndGates(unittest.TestCase):
    def test_walls_and_gates(self):
        rooms = [[float("inf"), -1, 0, float("inf")],
                 [float("inf"), float("inf"), float("inf"), -1],
                 [float("inf"), -1, float("inf"), -1],
                 [0, -1, float("inf"), float("inf")]]
        walls_and_gates(rooms)
        self.assertEqual([[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1],
                          [0, -1, 3, 4]], rooms)


class TestMazeSearchDfs(unittest.TestCase):
    def test_maze_search(self):
        maze_1 = [[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
                   1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,
                   0, 1, 1, 1, 0, 1]]
        self.assertEqual(37, find_path_dfs(maze_1))
        maze_2 = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
        self.assertEqual(14, find_path_dfs(maze_2))
        maze_3 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(-1, find_path_dfs(maze_3))


# --- Tests merged from test_topological.py ---

from algorithms.graph import topological_sort
from algorithms.graph import top_sort, top_sort_recursive


class TestTopSort(unittest.TestCase):
    def setUp(self):
        self.depGraph = {
            "a": ["b"],
            "b": ["c"],
            "c": ['e'],
            'e': ['g'],
            "d": [],
            "f": ["e", "d"],
            "g": []
        }

    def test_topsort(self):
        res = top_sort_recursive(self.depGraph)
        self.assertTrue(res.index('g') < res.index('e'))
        res = top_sort(self.depGraph)
        self.assertTrue(res.index('g') < res.index('e'))


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

"""
Collection of graph algorithms.
"""

from __future__ import annotations

from algorithms.data_structures.graph import DirectedEdge, DirectedGraph, Node
from algorithms.graph.a_star import a_star
from algorithms.graph.all_factors import get_factors, get_factors_iterative1, get_factors_iterative2
from algorithms.graph.all_pairs_shortest_path import (
    all_pairs_shortest_path,
)
from algorithms.graph.bellman_ford import bellman_ford
from algorithms.graph.check_bipartite import check_bipartite
from algorithms.graph.clone_graph import (
    UndirectedGraphNode,
    clone_graph,
    clone_graph1,
    clone_graph2,
)
from algorithms.graph.count_islands_bfs import count_islands
from algorithms.graph.count_islands_dfs import num_islands as num_islands_dfs
from algorithms.graph.count_islands_unionfind import num_islands as num_islands_unionfind
from algorithms.graph.dijkstra import Dijkstra
from algorithms.graph.find_all_cliques import find_all_cliques
from algorithms.graph.kahns_algorithm import Solution as KahnsSolution
from algorithms.graph.markov_chain import iterating_markov_chain, next_state
from algorithms.graph.maximum_flow import dinic, edmonds_karp, ford_fulkerson
from algorithms.graph.maximum_flow_bfs import maximum_flow_bfs
from algorithms.graph.maximum_flow_dfs import maximum_flow_dfs
from algorithms.graph.maze_search_bfs import maze_search
from algorithms.graph.maze_search_dfs import find_path as find_path_dfs
from algorithms.graph.minimum_spanning_tree import DisjointSet, Edge, kruskal
from algorithms.graph.pacific_atlantic import pacific_atlantic
from algorithms.graph.prims_minimum_spanning import prims_minimum_spanning
from algorithms.graph.satisfiability import solve_sat
from algorithms.graph.shortest_distance_from_all_buildings import shortest_distance
from algorithms.graph.sudoku_solver import Sudoku
from algorithms.graph.tarjan import Tarjan
from algorithms.graph.topological_sort_bfs import topological_sort
from algorithms.graph.topological_sort_dfs import top_sort, top_sort_recursive
from algorithms.graph.traversal import (
    bfs_traverse,
    dfs_traverse,
    dfs_traverse_recursive,
)
from algorithms.graph.walls_and_gates import walls_and_gates
from algorithms.graph.word_ladder import ladder_length

__all__ = [
    # a_star
    "a_star",
    # all_pairs_shortest_path
    "all_pairs_shortest_path",
    # bellman_ford
    "bellman_ford",
    # check_bipartite
    "check_bipartite",
    # clone_graph
    "UndirectedGraphNode",
    "clone_graph",
    "clone_graph1",
    "clone_graph2",
    # dijkstra
    "Dijkstra",
    # find_all_cliques
    "find_all_cliques",
    # graph
    "DirectedEdge",
    "DirectedGraph",
    "Node",
    # kahns_algorithm
    "KahnsSolution",
    # markov_chain
    "iterating_markov_chain",
    "next_state",
    # maximum_flow
    "dinic",
    "edmonds_karp",
    "ford_fulkerson",
    # maximum_flow_bfs
    "maximum_flow_bfs",
    # maximum_flow_dfs
    "maximum_flow_dfs",
    # minimum_spanning_tree
    "DisjointSet",
    "Edge",
    "kruskal",
    # prims_minimum_spanning
    "prims_minimum_spanning",
    # satisfiability
    "solve_sat",
    # tarjan
    "Tarjan",
    # traversal
    "bfs_traverse",
    "dfs_traverse",
    "dfs_traverse_recursive",
    # count_islands (bfs)
    "count_islands",
    # count_islands (dfs)
    "num_islands_dfs",
    # maze_search (bfs)
    "maze_search",
    # maze_search (dfs)
    "find_path_dfs",
    # word_ladder
    "ladder_length",
    # shortest_distance_from_all_buildings
    "shortest_distance",
    # topological_sort (bfs)
    "topological_sort",
    # all_factors
    "get_factors",
    "get_factors_iterative1",
    "get_factors_iterative2",
    # pacific_atlantic
    "pacific_atlantic",
    # sudoku_solver
    "Sudoku",
    # walls_and_gates
    "walls_and_gates",
    # topological_sort_dfs
    "top_sort",
    "top_sort_recursive",
    # count_islands_unionfind
    "num_islands_unionfind",
]

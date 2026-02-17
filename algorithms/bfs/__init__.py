"""
Collection of BFS-based algorithms.
"""

from __future__ import annotations

from algorithms.bfs.count_islands import count_islands
from algorithms.bfs.maze_search import maze_search
from algorithms.bfs.shortest_distance_from_all_buildings import shortest_distance
from algorithms.bfs.topological import topological_sort
from algorithms.bfs.word_ladder import ladder_length

__all__ = [
    "count_islands",
    "maze_search",
    "shortest_distance",
    "topological_sort",
    "ladder_length",
]

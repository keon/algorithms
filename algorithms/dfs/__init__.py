"""
Collection of DFS-based algorithms.
"""

from __future__ import annotations

from algorithms.dfs.all_factors import (
    get_factors,
    get_factors_iterative1,
    get_factors_iterative2,
)
from algorithms.dfs.count_islands import num_islands
from algorithms.dfs.maze_search import find_path
from algorithms.dfs.pacific_atlantic import pacific_atlantic
from algorithms.dfs.sudoku_solver import Sudoku
from algorithms.dfs.walls_and_gates import walls_and_gates

__all__ = [
    "get_factors",
    "get_factors_iterative1",
    "get_factors_iterative2",
    "num_islands",
    "find_path",
    "pacific_atlantic",
    "Sudoku",
    "walls_and_gates",
]

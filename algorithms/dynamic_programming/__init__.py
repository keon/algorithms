"""
Dynamic Programming Algorithms

A collection of dynamic programming algorithm implementations.
"""

from . import regex_matching
from .bitmask import tsp
from .buy_sell_stock import max_profit_naive, max_profit_optimized
from .climbing_stairs import climb_stairs, climb_stairs_optimized
from .coin_change import count
from .combination_sum import combination_sum_bottom_up, combination_sum_topdown
from .count_paths_dp import count_paths_dp, count_paths_memo, count_paths_recursive
from .edit_distance import edit_distance
from .egg_drop import egg_drop
from .fib import fib_iter, fib_list, fib_recursive
from .hosoya_triangle import hosoya, hosoya_testing
from .house_robber import house_robber
from .int_divide import int_divide
from .job_scheduling import Job, schedule
from .k_factor import find_k_factor
from .knapsack import Item, get_maximum_value
from .longest_common_subsequence import longest_common_subsequence
from .longest_increasing import (
    longest_increasing_subsequence,
    longest_increasing_subsequence_optimized,
    longest_increasing_subsequence_optimized2,
)
from .matrix_chain_order import matrix_chain_order
from .max_product_subarray import max_product, subarray_with_max_product
from .max_subarray import max_subarray
from .min_cost_path import min_cost
from .num_decodings import num_decodings, num_decodings2
from .planting_trees import planting_trees
from .regex_matching import is_match
from .rod_cut import cut_rod
from .word_break import word_break

__all__ = [
    # buy_sell_stock
    "max_profit_naive",
    "max_profit_optimized",
    # climbing_stairs
    "climb_stairs",
    "climb_stairs_optimized",
    # coin_change
    "count",
    # combination_sum
    "combination_sum_topdown",
    "combination_sum_bottom_up",
    # edit_distance
    "edit_distance",
    # egg_drop
    "egg_drop",
    # fib
    "fib_recursive",
    "fib_list",
    "fib_iter",
    # hosoya_triangle
    "hosoya",
    "hosoya_testing",
    # house_robber
    "house_robber",
    # int_divide
    "int_divide",
    # job_scheduling
    "Job",
    "schedule",
    # k_factor
    "find_k_factor",
    # knapsack
    "Item",
    "get_maximum_value",
    # longest_common_subsequence
    "longest_common_subsequence",
    # longest_increasing
    "longest_increasing_subsequence",
    "longest_increasing_subsequence_optimized",
    "longest_increasing_subsequence_optimized2",
    # matrix_chain_order
    "matrix_chain_order",
    # max_product_subarray
    "max_product",
    "subarray_with_max_product",
    # max_subarray
    "max_subarray",
    # min_cost_path
    "min_cost",
    # num_decodings
    "num_decodings",
    "num_decodings2",
    # planting_trees
    "planting_trees",
    # regex_matching
    "regex_matching",
    "is_match",
    # rod_cut
    "cut_rod",
    # word_break
    "word_break",
    # bitmask
    "tsp",
    # count_paths_dp
    "count_paths_dp",
    "count_paths_memo",
    "count_paths_recursive",
]

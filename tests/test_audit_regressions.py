"""Regression tests for defects found during the repository-wide audit."""

from __future__ import annotations

import importlib
import math

import pytest

from algorithms.common import TreeNode
from algorithms.graph.sudoku_solver import Sudoku
from algorithms.graph.transitive_closure_dfs import Graph
from algorithms.math.extended_gcd import extended_gcd
from algorithms.math.gcd import gcd, lcm
from algorithms.searching.search_rotate import search_rotate_recur
from algorithms.stack.ordered_stack import OrderedStack
from algorithms.tree.bst_delete_node import Solution
from algorithms.tree.max_path_sum import max_path_sum


@pytest.mark.parametrize(
    "module_name",
    [
        "algorithms.tree.bst_count_left_node",
        "algorithms.tree.bst_depth_sum",
        "algorithms.tree.bst_height",
        "algorithms.tree.bst_num_empty",
    ],
)
def test_tree_modules_import(module_name: str) -> None:
    importlib.import_module(module_name)


def test_sudoku_solution_respects_rows_columns_and_subgrids() -> None:
    board = [
        list("53..7...."),
        list("6..195..."),
        list(".98....6."),
        list("8...6...3"),
        list("4..8.3..1"),
        list("7...2...6"),
        list(".6....28."),
        list("...419..5"),
        list("....8..79"),
    ]

    assert Sudoku(board, 9, 9).solve()

    expected = set("123456789")
    groups = list(board)
    groups.extend([list(column) for column in zip(*board, strict=True)])
    groups.extend(
        [
            [board[row + i][column + j] for i in range(3) for j in range(3)]
            for row in (0, 3, 6)
            for column in (0, 3, 6)
        ]
    )
    assert all(set(group) == expected for group in groups)


@pytest.mark.parametrize("left,right", [(240, 46), (99, 78), (-25, 10)])
def test_extended_gcd_satisfies_bezout_identity(left: int, right: int) -> None:
    s, t, result = extended_gcd(left, right)

    assert result == math.gcd(left, right)
    assert left * s + right * t == result


def test_max_path_sum_handles_positive_and_negative_trees() -> None:
    root = TreeNode(
        -10,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    assert max_path_sum(root) == 42
    assert max_path_sum(TreeNode(-3)) == -3


def test_bst_delete_recurses_to_non_root_node() -> None:
    root = TreeNode(5, TreeNode(3), TreeNode(6))

    result = Solution().delete_node(root, 3)

    assert result is root
    assert result.left is None


def test_recursive_rotated_search_checks_singleton_range() -> None:
    values = [4, 5, 6, 7, 0, 1, 2]

    assert search_rotate_recur(values, 0, len(values) - 1, 0) == 4
    assert search_rotate_recur([1], 0, 0, 1) == 0


def test_ordered_stack_can_insert_new_minimum() -> None:
    stack = OrderedStack()
    for value in (3, 1, 2):
        stack.push(value)

    assert [stack.pop(), stack.pop(), stack.pop()] == [3, 2, 1]


def test_transitive_closure_handles_sink_and_isolated_vertices() -> None:
    graph = Graph(3)
    graph.add_edge(0, 1)

    assert graph.transitive_closure() == [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]


def test_gcd_rejects_mixed_numeric_types_and_lcm_is_integer() -> None:
    with pytest.raises(ValueError, match="not integers"):
        gcd(3.5, 2)

    result = lcm(8, 12)
    assert result == 24
    assert isinstance(result, int)

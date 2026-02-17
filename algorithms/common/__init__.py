"""Shared data types used across all algorithm categories.

These types are the connective tissue of the library — every algorithm
accepts and returns these types, making them composable.

    >>> from algorithms.common import TreeNode, ListNode, Graph
"""

from algorithms.common.tree_node import TreeNode
from algorithms.common.list_node import ListNode
from algorithms.common.graph import Graph

__all__ = ["TreeNode", "ListNode", "Graph"]

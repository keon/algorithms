"""Pythonic data structures and algorithms for education.

Shared types are available at the top level::

    >>> from algorithms import TreeNode, ListNode, Graph
    >>> from algorithms.data_structures import BinaryHeap, HashTable
    >>> from algorithms.graph import dijkstra
"""

from algorithms.common import Graph, ListNode, TreeNode

import algorithms.data_structures as data_structures  # noqa: F401

__all__ = ["TreeNode", "ListNode", "Graph", "data_structures"]

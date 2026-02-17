"""Graph Data Structures (re-export).

This module re-exports Node, DirectedEdge, and DirectedGraph from the
canonical location in ``algorithms.data_structures.graph`` for backward
compatibility.
"""

from algorithms.data_structures.graph import DirectedEdge, DirectedGraph, Node

__all__ = ["DirectedEdge", "DirectedGraph", "Node"]

"""
Clone an Undirected Graph

Each node contains a label and a list of its neighbours.  Three strategies
are provided: BFS-based, iterative DFS, and recursive DFS.

Reference: https://leetcode.com/problems/clone-graph/

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

import collections


class UndirectedGraphNode:
    """A node in an undirected graph."""

    def __init__(self, label: int) -> None:
        self.label = label
        self.neighbors: list[UndirectedGraphNode] = []

    def shallow_copy(self) -> UndirectedGraphNode:
        """Return a copy of this node without neighbours.

        Returns:
            A new node with the same label.
        """
        return UndirectedGraphNode(self.label)

    def add_neighbor(self, node: UndirectedGraphNode) -> None:
        """Append *node* to the neighbour list.

        Args:
            node: Neighbour to add.
        """
        self.neighbors.append(node)


def clone_graph1(node: UndirectedGraphNode | None) -> UndirectedGraphNode | None:
    """Clone a graph using BFS.

    Args:
        node: Any node in the original graph.

    Returns:
        The corresponding node in the cloned graph, or None.
    """
    if not node:
        return None
    node_copy = node.shallow_copy()
    dic: dict[UndirectedGraphNode, UndirectedGraphNode] = {node: node_copy}
    queue: collections.deque[UndirectedGraphNode] = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighbor_copy = neighbor.shallow_copy()
                dic[neighbor] = neighbor_copy
                dic[node].add_neighbor(neighbor_copy)
                queue.append(neighbor)
            else:
                dic[node].add_neighbor(dic[neighbor])
    return node_copy


def clone_graph2(node: UndirectedGraphNode | None) -> UndirectedGraphNode | None:
    """Clone a graph using iterative DFS.

    Args:
        node: Any node in the original graph.

    Returns:
        The corresponding node in the cloned graph, or None.
    """
    if not node:
        return None
    node_copy = node.shallow_copy()
    dic: dict[UndirectedGraphNode, UndirectedGraphNode] = {node: node_copy}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighbor_copy = neighbor.shallow_copy()
                dic[neighbor] = neighbor_copy
                dic[node].add_neighbor(neighbor_copy)
                stack.append(neighbor)
            else:
                dic[node].add_neighbor(dic[neighbor])
    return node_copy


def clone_graph(node: UndirectedGraphNode | None) -> UndirectedGraphNode | None:
    """Clone a graph using recursive DFS.

    Args:
        node: Any node in the original graph.

    Returns:
        The corresponding node in the cloned graph, or None.
    """
    if not node:
        return None
    node_copy = node.shallow_copy()
    dic: dict[UndirectedGraphNode, UndirectedGraphNode] = {node: node_copy}
    _dfs(node, dic)
    return node_copy


def _dfs(
    node: UndirectedGraphNode,
    dic: dict[UndirectedGraphNode, UndirectedGraphNode],
) -> None:
    """Recursively clone neighbours into *dic*.

    Args:
        node: Current node being cloned.
        dic: Mapping from original nodes to their clones.
    """
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighbor_copy = neighbor.shallow_copy()
            dic[neighbor] = neighbor_copy
            dic[node].add_neighbor(neighbor_copy)
            _dfs(neighbor, dic)
        else:
            dic[node].add_neighbor(dic[neighbor])

r"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
import collections


class UndirectedGraphNode:
    """
    A node in an undirected graph. Contains a label and a list of neighbouring
    nodes (initially empty).
    """

    def __init__(self, label):
        self.label = label
        self.neighbors = []

    def shallow_copy(self):
        """
        Return a shallow copy of this node (ignoring any neighbors)
        """
        return UndirectedGraphNode(self.label)

    def add_neighbor(self, node):
        """
        Adds a new neighbor
        """
        self.neighbors.append(node)


def clone_graph1(node):
    """
    Returns a new graph as seen from the given node using a breadth first search (BFS).
    """
    if not node:
        return None
    node_copy = node.shallow_copy()
    dic = {node: node_copy}
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in dic:  # neighbor is not visited
                neighbor_copy = neighbor.shallow_copy()
                dic[neighbor] = neighbor_copy
                dic[node].add_neighbor(neighbor_copy)
                queue.append(neighbor)
            else:
                dic[node].add_neighbor(dic[neighbor])
    return node_copy


def clone_graph2(node):
    """
    Returns a new graph as seen from the given node using an iterative depth first search (DFS).
    """
    if not node:
        return None
    node_copy = node.shallow_copy()
    dic = {node: node_copy}
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


def clone_graph(node):
    """
    Returns a new graph as seen from the given node using a recursive depth first search (DFS).
    """
    if not node:
        return None
    node_copy = node.shallow_copy()
    dic = {node: node_copy}
    dfs(node, dic)
    return node_copy


def dfs(node, dic):
    """
    Clones a graph using a recursive depth first search. Stores the clones in
    the dictionary, keyed by the original nodes.
    """
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighbor_copy = neighbor.shallow_copy()
            dic[neighbor] = neighbor_copy
            dic[node].add_neighbor(neighbor_copy)
            dfs(neighbor, dic)
        else:
            dic[node].add_neighbor(dic[neighbor])
